# Generated by Django 3.2.9 on 2021-11-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default='', verbose_name='movie trailer'),
            preserve_default=False,
        ),
    ]
