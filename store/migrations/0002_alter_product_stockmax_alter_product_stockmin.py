# Generated by Django 4.1 on 2022-12-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stockMax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stockMin',
            field=models.IntegerField(null=True),
        ),
    ]
