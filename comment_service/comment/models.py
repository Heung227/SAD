# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class book(models.Model):
    # The following are the fields of our table.

    content = models.CharField(max_length=50)

    # It will help to print the values.

    def __str__(self):
        return '%s' % (
            self.content
        )
