from datetime import date
from django.shortcuts import render
from .models import Post


all_posts = Post.objects.all().order_by("date")

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("date")[:3]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    tags = identified_post.tag.all()
    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "tags": tags
    })