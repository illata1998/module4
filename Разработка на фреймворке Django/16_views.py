from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from simple_blog.categories.models import Category
# BEGIN
from simple_blog.categories.forms import CategoryForm
# END


class IndexView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, 'categories/index.html', context={
            'categories': categories,
        })


class CategoryView(View):

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        return render(request, 'categories/category.html', context={
            'category': category,
        })


# BEGIN
class CategoryCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'categories/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_index')

        return render(request, 'categories/create.html', {'form': form})
# END
