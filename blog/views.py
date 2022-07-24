from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

class Index(ListView):
    #一覧表示するモデルを指定 object_listで取得可能
    model = Post

class Detail(DetailView):
    #objectで取得可能
    model = Post
# Create your views here.
