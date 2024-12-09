from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


@require_http_methods(['GET', 'POST'])
def index(request):
    # BEGIN
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'author': request.POST['author']
        }
        Article.objects.create(**data).save()
    articles = Article.objects.all()
    # END
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def article_view(request, id):
    # BEGIN
    article = Article.objects.filter(pk=id).first()
    if not article:
        raise Http404()
    # END
    return render(request, 'articles/article.html', context={'article': article})
