# Generated by Django 3.2.7 on 2021-10-01 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hopper', '0006_delete_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wod',
            name='users',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hopper.wod')),
            ],
        ),
    ]
