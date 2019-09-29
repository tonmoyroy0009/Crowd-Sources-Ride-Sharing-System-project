from .models import Post
from .forms import NewPostForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required
def createPost(request):
    if request.method == 'POST':
        new_post = NewPostForm(request.POST, request.FILES)
        if new_post.is_valid():
            new_post = new_post.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(
                request, f'new post created!')
        return redirect('post')
    else:
        content = {'form': NewPostForm()}
        return render(request, 'posts/create.html', content)


@login_required
def update(request, id):
    post = Post.objects.get(pk=id)
    if request.user == post.author:
        if request.method == 'POST':
            new_post = NewPostForm(
                request.POST, request.FILES, instance=post)
            if new_post.is_valid():
                new_post.save()
                messages.success(request, f'Post update successful!')
            return redirect('profile')
        else:
            content = {
                'form': NewPostForm(instance=post),
                'state': "update"
            }
            return render(request, 'posts/create.html', content)


@login_required
def delete(request, id):
    post = Post.objects.get(pk=id)
    if request.user == post.author:
        post.delete()
        messages.success(request, f'Post removed successfully!')
    return redirect('profile')


@login_required
def detail(request, id):
    try:
        post = Post.objects.get(pk=id)
    except ObjectDoesNotExist:
        post = None
    content = {'post': post}
    return render(request, 'posts/detail.html', content)


def posts(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)  # Show 5 items per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    content = {
        'posts': posts
        }
    return render(request, 'posts/post.html', content)
