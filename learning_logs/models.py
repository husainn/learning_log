from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.text[:50]+'...'

