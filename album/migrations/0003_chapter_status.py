# Generated by Django 2.0.6 on 2020-04-13 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_chapter_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
