#coding: utf-8
#from django.shortcuts import render


from blog.models import Post
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

# Create your views here.

