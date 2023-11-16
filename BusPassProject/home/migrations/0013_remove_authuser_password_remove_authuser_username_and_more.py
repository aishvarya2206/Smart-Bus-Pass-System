# Generated by Django 4.1 on 2023-04-08 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0012_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='authuser',
            name='username',
        ),
        migrations.AddField(
            model_name='authuser',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]