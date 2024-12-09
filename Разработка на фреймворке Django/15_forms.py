from django import forms
from .models import Article

# BEGIN
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']
# END
