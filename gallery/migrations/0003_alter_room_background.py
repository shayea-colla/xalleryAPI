# Generated by Django 4.2.3 on 2023-10-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0002_alter_room_background"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="background",
            field=models.ImageField(
                help_text="Set a background for the room",
                max_length=1000,
                upload_to="rooms_background/",
            ),
        ),
    ]
