# Generated by Django 4.1 on 2023-04-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_pass_college_alter_pass_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='verify_college_reject',
            field=models.BooleanField(default=False),
        ),
    ]