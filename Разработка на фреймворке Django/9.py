from django.db import models

# BEGIN
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Employee(models.Model):
    TRAINEE = 'TR'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CEO = 'CEO'

    POSITIONS = [
        (TRAINEE, 'Trainee'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (CEO, 'CEO'),
    ]

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=3, choices=POSITIONS, default=TRAINEE)
# END
