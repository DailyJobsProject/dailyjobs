from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

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
