# Generated by Django 4.1 on 2022-12-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_stockmax_alter_product_stockmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='form',
            field=models.CharField(choices=[('FL', 'FLACON'), ('BT', 'BOITE'), ('TB', 'TUBE'), ('CT', 'CARTON')], default='BOITE', max_length=20),
        ),
    ]