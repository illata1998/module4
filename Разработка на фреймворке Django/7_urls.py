from django.urls import path
from simple_blog.articles import views


urlpatterns = [
    # BEGIN
    path('', views.index),
    # END
]
