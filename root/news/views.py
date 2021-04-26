from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Post


def _list(request):
    return render(request, 'news/list.html', context={
        'all_posts': Post.objects.all()
    })


def create(request):
    if request.method == 'GET':
        return render(request, 'news/create.html', context={
            'form': PostForm()
        })
    elif request.method == 'POST':
        ready_form = PostForm(request.POST, request.FILES)
        ready_form.save()
        return redirect('/news/list')


def details(request, post_id):
    return render(request, 'news/details.html', context={
        'single_post': Post.objects.get(id=post_id)
    })


def edit(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'news/edit.html', context={
            'form': PostForm(instance=edit_post),
            'post': edit_post
        })
    elif request.method == 'POST':
        ready_form = PostForm(request.POST, request.FILES, instance=edit_post)
        if ready_form.is_valid():
                edit_post.title = ready_form.cleaned_data['title']
                edit_post.about = ready_form.cleaned_data['about']
                edit_post.content = ready_form.cleaned_data['content']
                edit_post.author = ready_form.cleaned_data['author']
                edit_post.source = ready_form.cleaned_data['source']
                edit_post.image = ready_form.cleaned_data['image']
                edit_post.save()
        return redirect('/news/list')


def delete(request, post_id):
    del_post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'news/delete.html', context={
            'del_post': del_post
        })

    elif request.method == 'POST':
        del_post.delete()
        return redirect('/news/list')



