from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy


from .forms import ApplicationForm

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import CompanyPost, Application
from django.contrib.auth import get_user_model

User = get_user_model()

class PostCreateView(LoginRequiredMixin, CreateView):
    fields = ('title', 'description')
    model = CompanyPost

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.image = self.request.FILES
        self.object.save()
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = CompanyPost
    template_name = 'posts/companypost_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView , self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        context['all_applicants'] = Application.objects.all().values_list('name', flat=True)
        context['identifiers'] = Application.objects.all().values_list('identifier', flat=True)
        return context

class PostListView(LoginRequiredMixin,ListView):
    model= CompanyPost
    template_name = 'posts/companypost_list.html'
    context_object_name = 'posts'
    queryset = CompanyPost.objects.all()

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = CompanyPost
    template_name = 'posts/companypost_delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('startpage')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyPost
    fields = ['title', 'description']
    template_name = 'posts/companypost_update.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('startpage')

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'posts/application_delete.html'
    context_object_name = 'application'

    def get_success_url(self):
        return reverse_lazy('posts:list')


@login_required
def post_apply(request, pk):
    post = get_object_or_404(CompanyPost, pk=pk)
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        form = ApplicationForm()
        application = form.save(commit=False)
        application.name = request.user
        application.post = post
        application.identifier += post.title + request.user.username
        application.save()
        return redirect('posts:detail', pk=post.pk)
    else:

        form = ApplicationForm()

    return render(request, 'posts/application_form.html', {'form': form})
