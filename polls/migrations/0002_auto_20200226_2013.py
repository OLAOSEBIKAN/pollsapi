# Generated by Django 3.0.3 on 2020-02-26 20:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Polls',
            new_name='Poll',
        ),
    ]