from django.db import models


class Vote(models.Model):
    subject = models.CharField(max_length=200)
    positive = models.BooleanField(default=True)

    @classmethod
    def in_favour(cls, subject):
        "Create a new vote in favour of the subject."
        # BEGIN
        return cls.objects.create(subject=subject)
        # END

    @classmethod
    def against(cls, subject):
        "Create a new vote against of the subject."
        # BEGIN
        return cls.objects.create(subject=subject, positive=False)
        # END
