from django.http import JsonResponse
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


#  PIE CHART
def chart_data(request):

    item = VisitedPagesCounter.objects.all()[0]

    dataset = [("home_views",item.home_views+5), ("careers_views",item.careers_views+15),
               ("videos_views",item.videos_views+25), ("news_views",item.news_views+50), ("hero_views",item.meet_your_hero_views+3)]

    print(dataset)
    views_counter = dict()
    for item in dataset:
        views_counter[item[0]] = item[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Page visited statistics'},
        'series': [{
            'name': 'Visits',
            'data': list(map(lambda row: {'name': row[0], 'y': row[1]}, dataset))
        }]
    }

    return JsonResponse(chart)


def admin_site(request):
    return render(request, 'admin_site.html')