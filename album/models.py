from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=20)
    score = models.SmallIntegerField()
    author = models.CharField(max_length=20)
    announcer = models.CharField(max_length=20)
    chapter_count = models.IntegerField()
    album_info = models.TextField()
    status = models.CharField(max_length=20)
    publish_time = models.DateTimeField()
    upload_time = models.DateTimeField()
    cover = models.ImageField(upload_to="album_picture")  # 封面


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    time_long = models.CharField(max_length=200)
    album_id = models.IntegerField()
    audio = models.ImageField(null=True,upload_to="audio")
    status = models.CharField(max_length=200,null=True)
    create_date = models.DateTimeField(auto_now_add=True, auto_created=True,null=True)
