# Generated by Django 3.1.4 on 2021-06-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawplayer', '0009_song_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='recommend',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='song',
            name='trend',
            field=models.CharField(max_length=3),
        ),
    ]