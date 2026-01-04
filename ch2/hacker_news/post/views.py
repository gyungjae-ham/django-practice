from django.http import HttpResponse
from django.shortcuts import render

from post.models import Post


def posts_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "post_list.html", context)