# Generated by Django 4.1.2 on 2022-11-04 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lct4', '0010_districts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('description', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Коды2',
                'verbose_name_plural': 'Коды2',
            },
        ),
        migrations.CreateModel(
            name='Nishas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='lct4.productnames')),
                ('region_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='lct4.regions')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='lct4.customusers')),
            ],
            options={
                'verbose_name': 'Нишы',
                'verbose_name_plural': 'Нишы',
            },
        ),
    ]
