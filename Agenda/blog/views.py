from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Pessoal
from .forms import PostForm, PostPessoal

from django.utils.timezone import localdate
from datetime import datetime
from events.models import Event


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()) \
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def pessoal_detail(request, pk):
    pessoa = get_object_or_404(Pessoal, pk=pk)
    return render(request, 'blog/pessoal_detail.html',  {'pessoa': pessoa})

def pessoal(request):
    if request.method == 'POST':
        form = PostPessoal(request.POST)
        if form.is_valid():
            pessoa = form.save(commit=False)

            pessoa.save()
            return redirect('pessoal_detail', pk=pessoa.pk)
    else:
        form = PostPessoal()
    return render(request, 'blog/pessoal.html', {'form': form})

def pessoal_list(request):
    pessoals = Pessoal.objects.filter()
    return render(request, 'blog/pessoal_list.html', {'pessoals': pessoals})
