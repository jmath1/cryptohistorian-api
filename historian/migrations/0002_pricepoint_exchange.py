# Generated by Django 2.1.7 on 2020-01-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historian', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricepoint',
            name='exchange',
            field=models.CharField(default='Default', max_length=30),
        ),
    ]
