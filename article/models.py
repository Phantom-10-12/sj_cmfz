from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=20,null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True,auto_created=True,auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guru_id = models.CharField(max_length=11, blank=True, null=True)
    new_img = models.CharField(max_length=100, blank=True, null=True)
    cate = models.IntegerField(null=True)

class Article_img(models.Model):
    article_picture = models.ImageField(upload_to='article_picture')
