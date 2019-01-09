from django.contrib import admin
from .models import Article, ExtraContent
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class ArticleAdmin(SummernoteModelAdmin):
    pass


class ExtraContentAdmin(SummernoteModelAdmin):
    pass


# myModels = [models.Article, models.ExtraContent]  # iterable list
# admin.site.register(myModels)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ExtraContent, ExtraContentAdmin)
