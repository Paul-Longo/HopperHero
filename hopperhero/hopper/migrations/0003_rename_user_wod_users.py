# Generated by Django 3.2.7 on 2021-09-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0002_wod_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wod',
            old_name='user',
            new_name='users',
        ),
    ]