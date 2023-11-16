# Generated by Django 4.1 on 2023-04-16 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_authuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='route_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_from_created', to='home.route'),
        ),
        migrations.AlterField(
            model_name='student',
            name='route_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_to_created', to='home.route'),
        ),
    ]
