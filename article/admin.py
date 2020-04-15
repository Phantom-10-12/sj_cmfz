from django.contrib import admin

# Register your models here.
from article import models
admin.site.register(models.Article_img)
admin.site.register(models.Article)
