# Generated by Django 3.1.3 on 2021-02-27 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["-date_joined"]},
        ),
    ]
