# Generated by Django 5.0.1 on 2024-01-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0004_alter_picture_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(
                help_text="Enter a name for the Room", max_length=150
            ),
        ),
    ]