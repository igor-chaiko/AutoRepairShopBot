# Generated by Django 4.2.4 on 2023-08-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание товара'),
        ),
    ]
