# Generated by Django 3.1.7 on 2021-04-22 21:54

from django.db import migrations, models
import hunchat.storage


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_auto_20210314_2205"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=hunchat.storage.get_image_file_path
            ),
        ),
    ]
