from .models import Article
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # article을 다 가져와서 목록을 보여준다.
    # 최신 글을 먼저 보여주고 싶다면?
    #articles = Article.objects.all()[::-1]
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
    # 받은 정보를 db에 저장
    article = Article()
    article.title = title
    article.content = content
    article.save()
    context = {
        'article': article,
    }
    #2 
    # Article.objects.create(title=title,content=content)
    #3
    # article=Article(title=title,content=content)
    # article.save()
    #글이 다 써졌으면, 해당 글 디테일 페이지로 redirecting
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
    #수정할 수 있는 화면을 보여줌
    # article_pk로 정보를 가져와서 넘겨주면 해결
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }
    return render(request,'articles/update.html',context)


def modify(request,article_pk):
    # 수정할 대상을 찾기
    article = Article.objects.get(pk=article_pk)
    # 수정할 데이터 가져오기
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 수정 대상을 수정할 데이터로 수정하기
    article.title=title
    article.content=content
    article.save()
    context={
        'article':article
    }
    return redirect('articles:detail',article.pk)