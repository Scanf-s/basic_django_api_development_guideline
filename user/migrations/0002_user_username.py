# Generated by Django 5.1.6 on 2025-02-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
