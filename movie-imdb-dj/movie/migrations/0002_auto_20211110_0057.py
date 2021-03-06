# Generated by Django 3.2.9 on 2021-11-10 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=50, verbose_name='cast'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DL', 'download links'), ('WL', 'watched links')], max_length=10, verbose_name='type')),
                ('links', models.URLField(verbose_name='links')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_links', to='movie.movie', verbose_name='movie')),
            ],
            options={
                'verbose_name': 'MovieLinks',
                'verbose_name_plural': 'MovieLinkss',
            },
        ),
    ]
