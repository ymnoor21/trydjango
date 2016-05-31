from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse


def post_list(request):
    queryset = Post.objects.all()

    context = {
        "all_posts": queryset
    }

    return render(request, "posts/list.html", context)


def post_detail(request, id):
    queryset = get_object_or_404(Post, id=id)

    context = {
        "post": queryset
    }

    return render(request, "posts/detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        return HttpResponseRedirect(reverse('posts:detail', args=[instance.id]))


    context = {
        "form": form,
        "title": "Create new post",
        "cmd": "create",
    }

    return render(request, "posts/form.html", context)


def post_edit(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
        "title": instance.title,
        "instance": instance,
        "cmd": "edit",
    }

    return render(request, "posts/form.html", context)


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
