from django.urls import path
from . import views 

urlpatterns = [
    path('artists/', views.artist_list_create),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/<int:artist_pk>/music/', views.create_music),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_detail_update_delete),
]
