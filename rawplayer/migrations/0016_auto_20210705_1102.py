# Generated by Django 3.1.4 on 2021-07-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawplayer', '0015_auto_20210704_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='history_id',
            new_name='hist_id',
        ),
        migrations.AlterField(
            model_name='history',
            name='music_id',
            field=models.CharField(default='', max_length=10000000),
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
    ]
