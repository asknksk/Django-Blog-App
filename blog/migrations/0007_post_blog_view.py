# Generated by Django 4.1 on 2022-09-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_blog_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_view',
            field=models.IntegerField(default=0),
        ),
    ]