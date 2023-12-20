# Generated by Django 4.2.7 on 2023-12-20 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("realEstateApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="last name"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="username"
                    ),
                ),
                ("password", models.CharField(max_length=255, verbose_name="password")),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "profile_photo",
                    models.ImageField(blank=True, null=True, upload_to="images"),
                ),
                (
                    "favorite_properties",
                    models.ManyToManyField(
                        related_name="custom_user_favorite_properties",
                        to="realEstateApp.property",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserFavorites",
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
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="custom_user_favorite_property",
                        to="realEstateApp.property",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]
