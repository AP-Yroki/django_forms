from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form),
    path('postuser/', views.postuser),
    path('', views.index),
    path('appointment/', views.appointment),
    path('order/', views.order),
    path('news/', views.news_list, name='news_list'),
    path('add/', views.add_news, name='add_news'),
]