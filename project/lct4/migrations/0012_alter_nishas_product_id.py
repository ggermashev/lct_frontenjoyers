# Generated by Django 4.1.2 on 2022-11-04 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lct4', '0011_productnames_nishas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nishas',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='lct4.codes'),
        ),
    ]