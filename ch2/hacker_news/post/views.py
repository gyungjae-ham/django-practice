from django.http import HttpResponse

from post.models import Post


def posts_view(request):
    posts = Post.objects.all()
    result = ", ".join([p.title for p in posts])
    return HttpResponse(result)