# Generated by Django 4.2.7 on 2023-12-05 23:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("realEstateApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="property",
            old_name="image",
            new_name="property_images",
        ),
    ]
