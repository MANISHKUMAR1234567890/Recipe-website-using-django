# Generated by Django 4.2.16 on 2024-09-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="veg_recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_procedure", models.TextField(max_length=2000)),
                ("recipe_image", models.ImageField(upload_to="veg_recipe")),
            ],
        ),
    ]
