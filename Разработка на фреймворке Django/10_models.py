from django.db import models

# BEGIN
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
# END
