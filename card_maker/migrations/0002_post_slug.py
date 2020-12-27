# Generated by Django 3.1.4 on 2020-12-26 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('card_maker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
    ]