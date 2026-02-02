from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # Use the project-level templates/index.html
    template_name = "index.html"
    paginate_by = 6

    