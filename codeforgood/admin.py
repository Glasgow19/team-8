from django.contrib import admin
from codeforgood.models import NewsArticle,RoleModel,VideoArticle,VisitedPagesCounter


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'picture', 'url')

class RoleModelAdmin(admin.ModelAdmin):
    list_display = ('title','picture','gender','ethnicity','position','description','url')

class VideoArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','views')

class VisitedPagesCounterPage(admin.ModelAdmin):
    exclude = ()


admin.site.register(NewsArticle, NewsArticleAdmin)
admin.site.register(RoleModel, RoleModelAdmin)
admin.site.register(VideoArticle, VideoArticleAdmin)
admin.site.register(VisitedPagesCounter, VisitedPagesCounterPage)
