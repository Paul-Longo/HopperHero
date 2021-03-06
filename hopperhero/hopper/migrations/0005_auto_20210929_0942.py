# Generated by Django 3.2.7 on 2021-09-29 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hopper', '0004_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='like',
            field=models.ManyToManyField(to='hopper.Wod'),
        ),
        migrations.AddField(
            model_name='likes',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
