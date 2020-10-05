from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def article_list_create(request):
    if request.method == 'GET': #list
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    else: #create
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 

@api_view(['GET','DELETE','PUT'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if request.method == 'GET': #detail
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE': #delete
        article.delete()
        return Response({'id': article_pk},status=status.HTTP_204_NO_CONTENT)
    else: #update
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)