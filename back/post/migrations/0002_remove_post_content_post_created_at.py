# Generated by Django 5.0 on 2023-12-22 12:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="content",
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]