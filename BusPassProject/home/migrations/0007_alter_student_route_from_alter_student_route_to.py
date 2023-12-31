# Generated by Django 4.1 on 2023-04-02 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_student_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='route_from',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_from_created', to='home.route'),
        ),
        migrations.AlterField(
            model_name='student',
            name='route_to',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_to_created', to='home.route'),
        ),
    ]
