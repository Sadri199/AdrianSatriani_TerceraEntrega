# Generated by Django 5.1.1 on 2024-10-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_mainactor_moviesdb_main_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdb',
            name='plot',
            field=models.CharField(max_length=100),
        ),
    ]
