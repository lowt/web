#coding: utf-8
#from django.shortcuts import render


from blog.models import Post, Comment
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = Post

class CommentDetailView(DetailView):
  model = Comment

# Create your views here.
