# Generated by Django 3.1.3 on 2021-02-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster',
            field=models.ImageField(blank=True, height_field='poster_height', null=True, upload_to='images', width_field='poster_width'),
        ),
        migrations.AddField(
            model_name='video',
            name='poster_height',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='poster_width',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
    ]
