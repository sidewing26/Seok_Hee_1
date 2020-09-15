from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Blog

# Create your views here.

class BlogView(ListView):
    model=Blog

class BlogCreate(CreateView):
    model=Blog
    fields=['title', 'body']
    success_url=reverse_lazy('list')

class BlogDetail(DetailView):
    model=Blog

class BlogUpdate(UpdateView):
    model=Blog
    fields=['title', 'body']
    template_name_suffix = '_update_form'
    success_url=reverse_lazy('list')

class BlogDelete(DeleteView):
    model=Blog
    success_url=reverse_lazy('list')