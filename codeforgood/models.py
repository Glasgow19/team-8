from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=30)
    #link = models.CharField(max_length=50)
    picture = models.ImageField()
    description = models.CharField(max_length=160)
    date = models.DateField()