from django.views.generic import ListView, DetailView # new
from .models import Post
from django.views.generic.edit import CreateView, UpdateView
class BlogListView(ListView):
 model = Post
 template_name = "home.html"
class BlogDetailView(DetailView): # new
 model = Post
 template_name = "post_detail.html"

class BlogCreateView(CreateView): # new
 model = Post
 template_name = "post_new.html"
 fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
 model = Post
 template_name = "post_edit.html"
 fields = ["title", "body"]



