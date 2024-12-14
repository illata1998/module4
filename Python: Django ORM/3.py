from django.db import models


# BEGIN
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# END
