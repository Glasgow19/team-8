from django.shortcuts import render, HttpResponse
from django.views import View
from .models import NewsArticle, RoleModel, VideoArticle, VisitedPagesCounter
from .forms import RoleModelsForm

# When a View is called first we increment
class IndexPage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0] # Since there's only one
        v.home_views += 1
        v.save()

        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class NewsPage(View):
    template_name = 'news.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.news_views += 1
        v.save()

        news_articles = NewsArticle.objects.all()
        context = {"news_articles": news_articles}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class CareersPage(View):
    template_name = 'careers.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.careers_views += 1
        v.save()

        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class VideosPage(View):
    template_name = 'videos.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.videos_views += 1
        v.save()

        video_articles = VideoArticle.objects.all()
        context = {"video_articles" : video_articles}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class ContactPage(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.contact_views += 1
        v.save()

        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class HeroPage(View):
    template_name = 'meet_your_hero.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.meet_your_hero_views += 1
        v.save()

        form = RoleModelsForm(request.POST)
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        context = {'rolemodels': {}}
        form = RoleModelsForm(request.POST)
        if form.is_valid():
            context = {'form': form, 'rolemodels': RoleModel.objects.filter(ethnicity=form.cleaned_data["ethnicity"], gender=form.cleaned_data["gender"])}
        return render(request, self.template_name, context=context)


class PlayPage(View):
    template_name = 'Unity_Game/index.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.play_views += 1
        v.save()

        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)