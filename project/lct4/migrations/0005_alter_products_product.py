# Generated by Django 4.1.2 on 2022-11-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lct4', '0004_remove_products_somenum1_remove_products_somenum2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product',
            field=models.CharField(max_length=16),
        ),
    ]
