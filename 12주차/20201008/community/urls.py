from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('',views.main, name='main'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.create, name='create'),
    path('reviews/<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:review_pk>/like_list/', views.like_list, name='like_list'),
    path('<int:review_pk>/like_detail/', views.like_detail, name='like_detail'),
    path('search/', views.search, name='search'),
]