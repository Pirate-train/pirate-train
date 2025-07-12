from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.game_list, name='game_list'),
    path('games/<slug:slug>/', views.game_detail, name='game_detail'),
    path('search/', views.search, name='search'),
]