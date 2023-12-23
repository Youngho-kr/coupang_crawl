# Generated by Django 5.0 on 2023-12-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0005_rename_title_post_tmp_remove_post_content"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Save_crawl",
        ),
        migrations.RemoveField(
            model_name="post",
            name="tmp",
        ),
        migrations.AddField(
            model_name="post",
            name="discount_percent",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="post",
            name="name",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="post",
            name="new_price",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="post",
            name="old_price",
            field=models.TextField(default=""),
        ),
    ]
