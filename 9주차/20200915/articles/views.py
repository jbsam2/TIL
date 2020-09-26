from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST,require_http_methods
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html',context)

@require_http_methods(['GET', 'POST'])
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, files=request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request,'articles/update.html',context)


@require_POST
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')