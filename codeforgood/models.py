from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    return "%s"%filename

class NewsArticle(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=300)
    picture = models.ImageField(upload_to=upload_to, blank=True)
    description = models.CharField(max_length=160)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class RoleModel(models.Model):
    name = models.CharField(max_length=70)
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
    future_self_views = models.IntegerField(default=0)


class FutureSelfRequest(models.Model):
    story = models.CharField(max_length=350)
    email = models.CharField(max_length=60)