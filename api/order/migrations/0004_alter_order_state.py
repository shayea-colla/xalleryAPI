# Generated by Django 4.2.3 on 2023-12-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_replay_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="state",
            field=models.BooleanField(default=None, null=True),
        ),
    ]
