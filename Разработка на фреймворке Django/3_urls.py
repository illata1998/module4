from django.urls import path
from simple_blog import views

urlpatterns = [
    path('', views.index, name='index'),
    # BEGIN
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    # END
]
