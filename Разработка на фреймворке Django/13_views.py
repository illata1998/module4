from django.shortcuts import render
from django.views import View
from simple_blog.categories.models import Category


# BEGIN
class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })
# END
