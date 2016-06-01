from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse


def post_list(request):
    posts = Post.objects.all()

    context = {
        "title": "Posts List",
        "posts": posts
    }

    return render(request, "posts/list.html", context)


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)

    context = {
        "title": "Post Detail",
        "post": post
    }

    return render(request, "posts/detail.html", context)


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(request, "Post created successfully.")
        return HttpResponseRedirect(
            reverse('posts:detail', kwargs={"id": instance.id})
        )

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

        messages.success(request, "Post saved successfully.")
        return HttpResponseRedirect(
            reverse('posts:detail', kwargs={"id": instance.id})
        )

    context = {
        "form": form,
        "title": instance.title,
        "post": instance,
        "cmd": "edit",
    }

    return render(request, "posts/form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post deleted.")
    return redirect("posts:list")
