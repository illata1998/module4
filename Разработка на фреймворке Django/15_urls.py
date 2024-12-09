from django.urls import path
from simple_blog.articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
    # BEGIN
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    # END
]
