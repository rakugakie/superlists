from django.db import models


class List(models.Model):
    url = models.URLField(max_length=100, default='')

    def __str__(self):
        return self.url


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

