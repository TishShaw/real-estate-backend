# Generated by Django 4.2.7 on 2023-12-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("realEstateApp", "0002_alter_propertyimage_property"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="type",
            field=models.CharField(default="", max_length=100, null=True),
        ),
    ]
