# Generated by Django 4.2.2 on 2023-06-30 04:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Admin", "0002_product_tb"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product_tb",
            name="Admin",
        ),
    ]
