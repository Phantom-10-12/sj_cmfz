# Generated by Django 2.0.6 on 2020-04-12 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='cate',
            field=models.IntegerField(null=True),
        ),
    ]