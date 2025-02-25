from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import NewsArticle, RoleModel, VideoArticle, VisitedPagesCounter, FutureSelfRequest
from .forms import RoleModelsForm, NewsArticleForm, FutureSelfForm
from django.views.decorators.csrf import csrf_exempt


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

class FutureSelf(View):
    template_name = 'future_self.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.future_self_views += 1
        v.save()

        form = RoleModelsForm(request.POST)
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = FutureSelfForm(request.POST)
        if form.is_valid():
            future_self = form.save()
            future_self.save()
            context["message"] = "Added future self request succesfully."
        form = RoleModelsForm(request.POST)
        context["form"] = form
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
        context = {}
        rolemodels = []
        form = RoleModelsForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["ethnicity"]=="All" and form.cleaned_data["gender"]=="All":
                rolemodels = RoleModel.objects.all()
            elif form.cleaned_data["ethnicity"]=="All":
                rolemodels = RoleModel.objects.filter(gender=form.cleaned_data["gender"])
            elif form.cleaned_data["gender"]=="All":
                rolemodels = RoleModel.objects.filter(ethnicity=form.cleaned_data["ethnicity"])
            else:
                rolemodels = RoleModel.objects.filter(ethnicity=form.cleaned_data["ethnicity"],
                                                      gender=form.cleaned_data["gender"])

        context = {'form': form, 'rolemodels': rolemodels}
        return render(request, self.template_name, context=context)


class PlayPage(View):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        v = VisitedPagesCounter.objects.all()[0]  # Since there's only one
        v.play_views += 1
        v.save()

        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)


class DisplayFutureSelf(View):
    template_name = 'display_future.html'

    def get(self, request, *args, **kwargs):
        f = FutureSelfRequest.objects.all();

        context = {"display_future":f}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        context = {}
        return render(request, self.template_name, context=context)

class AddNewsArticle(View):
    template_name = 'add_news_article.html'
    form = NewsArticleForm()

    def get(self, request, *args, **kwargs):
        context = {"form" : self.form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = NewsArticleForm(request.POST, request.FILES)
        context = {"form" : form}
        if form.is_valid():
            # Create the new article from the form's input
            af = form.save(commit=False)

            # We also need to store the uploaded image file
            if 'image' in request.FILES:
                af.picture = request.FILES['picture']
            af.save()

            context["form"] = NewsArticleForm()
            context["message"] = "Article added successfully."
        else:
            print(form)
        return render(request, self.template_name, context=context)


#  PIE CHART
def chart_data(request):

    item = VisitedPagesCounter.objects.all()[0]

    dataset = [("Careers Views", item.careers_views),
               ("Videos Views", item.videos_views), ("News Views", item.news_views),
               ("Hero Views", item.meet_your_hero_views), ("Game Views", item.play_views)]

    total_visits = item.home_views
    views_counter = dict()
    for item in dataset:
        views_counter[item[0]] = item[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': 'Total Website Visits: ' + str(total_visits)},
        'series': [{
            'name': 'Visits',
            'data': list(map(lambda row: {'name': row[0], 'y': row[1]}, dataset))
        }]
    }

    return JsonResponse(chart)


def admin_site(request):
    videos = VideoArticle.objects.order_by('-views')[:10]
    video_page_views = VisitedPagesCounter.objects.all()[0].videos_views
    video_views_ratio = []

    news_articles = NewsArticle.objects.order_by('-views')[:10]
    news_page_views = VisitedPagesCounter.objects.all()[0].news_views
    news_views_ratio = []

    for article in news_articles:
        news_views_ratio.append(article.views*100//news_page_views)

    for video in videos:
        video_views_ratio.append(video.views*100//video_page_views)

    videos = zip(videos,video_views_ratio)
    news_articles = zip(news_articles,news_views_ratio)
    context = {"videos": videos, "news_articles": news_articles}
    return render(request, 'admin_site.html', context)

@csrf_exempt
def IncrementNewsArticleView(request):

    if request.method=="POST":
        article_pk = request.POST.get("pk")
        status = False

        try:
            n = NewsArticle.objects.get(pk=article_pk)
        except:
            n = None
        if n:
            n.views += 1
            n.save()
            status = True

        return JsonResponse({'status': status})

# This method is working as intended, but we were
# having issues with detecting clicks on youtube embeded
# videos (iframes). We were not able to call a JS
# function once we clicked one.
@csrf_exempt
def IncrementVideoArticleView(request):

    if request.method=="POST":
        video_pk = request.POST.get("pk")
        status = False

        try:
            v = VideoArticle.objects.get(pk=video_pk)
        except:
            v = None
        if v:
            v.views += 1
            v.save()
            status = True

        return JsonResponse({'status': status})