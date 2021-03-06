# Generated by Django 3.2.9 on 2021-11-10 09:26

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20211110_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AC', 'action'), ('DR', 'drama'), ('RM', 'romance'), ('CM', 'comedy')], max_length=10, verbose_name='category'),
        ),
    ]
