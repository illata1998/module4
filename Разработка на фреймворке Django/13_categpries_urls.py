from django.urls import path
from simple_blog.categories import views


urlpatterns = [
    # BEGIN
    path('', views.IndexView.as_view(), name='categories_index'),
    # END
]
