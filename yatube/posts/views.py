from django.shortcuts import get_object_or_404, render

from .models import Group, Post

DISPLAY_RECORDS: int = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    group = Group.objects.get(title=group)
    posts = (group.posts.select_related('group', 'author').filter(group=group)
             [:DISPLAY_RECORDS])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
