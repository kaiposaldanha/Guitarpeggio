# Generated by Django 4.2.5 on 2023-10-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_product_imagem"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="type",
            field=models.CharField(default="Intrumento", max_length=64),
        ),
    ]
