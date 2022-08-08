from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

class Index(ListView):
    #一覧表示するモデルを指定 object_listで取得可能
    model = Post

class Detail(DetailView):
    #objectで取得可能
    model = Post

from django.views.generic.edit import CreateView

#CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = Post

    #編集対象にするフィールド
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    
    success_url = "/"
