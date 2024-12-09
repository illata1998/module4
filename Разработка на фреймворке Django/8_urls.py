from django.urls import path
from simple_blog.articles import views


urlpatterns = [
    path('', views.index),
    # BEGIN
    path('<int:id>/', views.article_view),
    # END
]
