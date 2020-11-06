# Generated by Django 3.0 on 2020-11-05 16:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_comment_users_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='posts_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='comments_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
