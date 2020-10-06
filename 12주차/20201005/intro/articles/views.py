from django.shortcuts import render
from django.core import serializers
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import Article
from articles.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def article_list_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article_list_html.html', context)


def article_list_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    return JsonResponse(articles_json, safe=False)


def article_list_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize("json", articles)
    return HttpResponse(data, content_type='application/json')

@api_view(['GET'])
def article_list_json_3(request):
    article = Article.objects.get(pk=1)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)