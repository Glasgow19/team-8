from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from codeforgood import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('news/', views.NewsPage.as_view(), name='news'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('videos/', views.VideosPage.as_view(), name='videos'),
    path('careers/', views.CareersPage.as_view(), name='careers'),
    path('meet_your_hero/', views.HeroPage.as_view(), name='meet_your_hero'),
]
