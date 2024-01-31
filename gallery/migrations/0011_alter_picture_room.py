# Generated by Django 5.0.1 on 2024-01-28 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0010_alter_room_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picture",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pictures",
                to="gallery.room",
            ),
        ),
    ]
