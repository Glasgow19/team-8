from django.db import models


class NewsArticle(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=300)
    picture = models.ImageField()
    description = models.CharField(max_length=160)
    views = models.IntegerField()


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
    url = models.CharField(max_length=300)
    views = models.IntegerField()


class VisitedPagesCounter(models.Model):
    # Each field represents the view count for a specific page
    # (ie. home_views = Index Page views)
    home_views = models.IntegerField(default=0)
    careers_views = models.IntegerField(default=0)
    contact_views = models.IntegerField(default=0)
    meet_your_hero_views = models.IntegerField(default=0)
    news_views = models.IntegerField(default=0)
    videos_views = models.IntegerField(default=0)
    play_views = models.IntegerField(default=0)
