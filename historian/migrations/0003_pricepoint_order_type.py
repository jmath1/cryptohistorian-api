# Generated by Django 2.1.7 on 2020-01-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historian', '0002_pricepoint_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricepoint',
            name='order_type',
            field=models.CharField(default='No Order Type', max_length=5),
        ),
    ]
