# Generated by Django 3.1.7 on 2021-04-22 21:54

from django.db import migrations, models
import hunchat.storage


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0003_auto_20210227_1337"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="file",
            field=models.FileField(upload_to=hunchat.storage.get_video_file_path),
        ),
        migrations.AlterField(
            model_name="video",
            name="poster",
            field=models.ImageField(
                blank=True,
                height_field="poster_height",
                null=True,
                upload_to=hunchat.storage.get_image_file_path,
                width_field="poster_width",
            ),
        ),
    ]
