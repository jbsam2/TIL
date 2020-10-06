from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title',)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title', 'content', 'created_at', 'updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields = ('id','content','article',)
        read_only_fields = ('article',)