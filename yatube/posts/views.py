from django.shortcuts import get_object_or_404, render

from .models import Group, Post

DISPLAY_RECORDS: int = 10


def index(request):
    posts = (Post.objects.select_related('group', 'author').all()
             [:DISPLAY_RECORDS])
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = (group.posts.select_related('group', 'author').all()
             [:DISPLAY_RECORDS])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
