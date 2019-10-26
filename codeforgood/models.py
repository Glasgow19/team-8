from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=30)
    #link = models.CharField(max_length=50)
    picture = models.ImageField()
    description = models.CharField(max_length=160)
    date = models.DateField()


class RoleModel(models.Model):
    title = models.CharField(max_length=60)
    picture = models.ImageField()
    gender = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    description = models.CharField(max_length=160)
    url = models.CharField(max_length=300)


class VideoArticle(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=160)
    picture = models.ImageField()
    url = models.CharField(max_length=300)