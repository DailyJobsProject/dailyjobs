from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView

from .models import CompanyPost


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = CompanyPost

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.picture = self.request.FILES
        self.object.save()
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = CompanyPost
    template_name = 'profiles/companypost_detail.html'






