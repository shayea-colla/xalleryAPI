# Generated by Django 4.2.3 on 2023-12-02 07:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0004_alter_order_state"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="reciever",
            new_name="receiver",
        ),
    ]