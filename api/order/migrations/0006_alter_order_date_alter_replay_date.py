# Generated by Django 4.2.3 on 2023-12-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0005_rename_reciever_order_receiver"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="replay",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
