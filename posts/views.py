from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views.generic import CreateView, DetailView, ListView

from .models import CompanyPost


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

class PostListView(LoginRequiredMixin,ListView):
    model= CompanyPost
    template_name= 'posts/companypost_list.html'
    context_object_name = 'posts'
    queryset = CompanyPost.objects.all()
