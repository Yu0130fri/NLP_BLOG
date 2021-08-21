from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<slug:pk>', views.show_article, name='show_article'),
]