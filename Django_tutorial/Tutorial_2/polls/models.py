import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date and time published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):              # __str__ on Python 3
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __str__ on Python 3
        return self.choice_text
