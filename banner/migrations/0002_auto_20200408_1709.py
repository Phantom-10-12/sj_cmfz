# Generated by Django 2.0.6 on 2020-04-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='create_time',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
