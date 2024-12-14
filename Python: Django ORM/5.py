from django.db import models


class Vote(models.Model):
    subject = models.CharField(max_length=200)
    positive = models.BooleanField(default=True)

    @classmethod
    def in_favour(cls, subject):
        "Create a new vote in favour of the subject."
        return cls.objects.create(subject=subject)

    @classmethod
    def against(cls, subject):
        "Create a new vote against of the subject."
        return cls.objects.create(subject=subject, positive=False)

    @classmethod
    def results_for(cls, subject):
        "Return the voting results for the subject."
        # BEGIN
        subject_votes = cls.objects.filter(subject=subject)
        return {
            'in favour': subject_votes.filter(positive=True).count(),
            'against': subject_votes.filter(positive=False).count(),
        }
        # END
