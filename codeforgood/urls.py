from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from codeforgood import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('news/', views.NewsPage.as_view(), name='news'),
    path('videos/', views.VideosPage.as_view(), name='videos'),
    path('meet_your_hero/', views.HeroPage.as_view(), name='meet_your_hero'),
    path('play/', views.PlayPage.as_view(), name='play'),
    path('admin_site/', views.admin_site, name='admin_site'),
    path('admin_site/data/', views.chart_data, name='chart_data'),
]
