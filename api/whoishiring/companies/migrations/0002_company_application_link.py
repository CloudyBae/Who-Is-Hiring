# Generated by Django 4.2 on 2023-04-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="application_link",
            field=models.URLField(blank=True),
        ),
    ]
