# Generated by Django 3.2.9 on 2021-11-10 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='movie_banner', verbose_name='banner'),
        ),
    ]
