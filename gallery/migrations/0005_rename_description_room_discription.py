# Generated by Django 5.0.1 on 2024-03-03 15:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0004_rename_discription_room_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="description",
            new_name="discription",
        ),
    ]
