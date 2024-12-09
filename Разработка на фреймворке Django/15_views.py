from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from simple_blog.articles.models import Article
from simple_blog.articles.forms import ArticleForm


# BEGIN
class ArticleCreateView(View):
    template_name = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
        else:
            return render(request, self.template_name, {'form': form})
# END

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/article.html', context={
            'article': article,
        })
