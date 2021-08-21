from django.urls import path

from . import views


app_name = 'nlp_django'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
]