from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework import viewsets

from .forms import ApplicationForm, CompanyPostForm

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import CompanyPost, Application
from django.contrib.auth import get_user_model

from .serializers import CompanyPostSerializer, ApplicationSerializer

User = get_user_model()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = CompanyPost
    form_class = CompanyPostForm
    template_name = 'posts/companypost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'pk': self.pk})

class PostDetailView(DetailView):
    model = CompanyPost
    template_name = 'posts/companypost_detail.html'

    def get_context_data(self, **kwargs):
        from django.apps import apps
        Companies = apps.get_model('users', 'Company')

        context = super(PostDetailView , self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        context['all_applicants'] = Application.objects.all().values_list('name', flat=True)
        context['identifiers'] = Application.objects.all().values_list('identifier', flat=True)
        context['companies'] = Companies.objects.all()
        context['post_titles'] = CompanyPost.objects.all().values_list('title', flat=True)
        return context


class PostListView(ListView):
    model= CompanyPost
    template_name = 'posts/companypost_list.html'
    context_object_name = 'posts'
    queryset = CompanyPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostListView , self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        context['identifiers'] = Application.objects.all().values_list('identifier', flat=True)
        return context

class EmployeeApplicationsListView(LoginRequiredMixin,ListView):
    model= CompanyPost
    template_name = 'posts/employee_applications_list.html'
    context_object_name = 'posts'
    queryset = CompanyPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeeApplicationsListView, self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        context['identifiers'] = Application.objects.all().values_list('identifier', flat=True)
        return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = CompanyPost
    template_name = 'posts/companypost_delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('posts:list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = CompanyPost
    form_class = CompanyPostForm
    template_name = 'posts/companypost_update.html'
    context_object_name = 'posts'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={'pk': self.pk})

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'posts/application_delete.html'
    context_object_name = 'application'

    def get_success_url(self):
        return reverse_lazy('posts:list')


@login_required
def post_apply(request, pk):
    post = get_object_or_404(CompanyPost, pk=pk)
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

class CompanyPostViewSet(viewsets.ModelViewSet):
    queryset = CompanyPost.objects.all().order_by('user')
    serializer_class = CompanyPostSerializer




class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('identifier')
    serializer_class = ApplicationSerializer

