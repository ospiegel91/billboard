from __future__ import unicode_literals
from django.utils.translation import gettext as _
from django.db import models

# Create your models here.
import datetime


class Message(models.Model):
    date = models.DateField(_("Date"), default=datetime.date.today)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=600)
    author = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Message"

    def __str__(self):
        return self.title