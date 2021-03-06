from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    path('<int:article_pk>/edit/', views.update, name='update'),
    path('modify/<int:article_pk>/', views.modify, name='modify'),
]