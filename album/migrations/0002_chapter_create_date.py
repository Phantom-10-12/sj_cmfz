# Generated by Django 2.0.6 on 2020-04-13 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='create_date',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, null=True),
        ),
    ]
