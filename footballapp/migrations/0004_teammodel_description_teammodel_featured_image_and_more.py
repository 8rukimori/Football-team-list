# Generated by Django 4.1.2 on 2022-10-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("footballapp", "0003_alter_teammodel_established_alter_teammodel_hometown"),
    ]

    operations = [
        migrations.AddField(
            model_name="teammodel",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="teammodel",
            name="featured_image",
            field=models.ImageField(blank=True, default=None, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="teammodel",
            name="achievement",
            field=models.TextField(blank=True, null=True),
        ),
    ]
