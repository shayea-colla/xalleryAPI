# Generated by Django 4.2.3 on 2023-11-25 07:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0004_alter_room_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-created_at"]},
        ),
    ]