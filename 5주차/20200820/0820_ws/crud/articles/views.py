from .models import Article
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.create(title=title,content=content)
    return redirect('articles:detail', article.pk)


def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html',context)


def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request,'articles/edit.html',context)


def modify(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    article.title=title
    article.content=content
    article.save()
    context={
        'article':article
    }
    return redirect('articles:detail',article.pk)