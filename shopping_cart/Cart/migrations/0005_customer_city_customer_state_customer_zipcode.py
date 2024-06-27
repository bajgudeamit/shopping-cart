# Generated by Django 4.2.1 on 2023-06-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_order_subtotal_amount_order_tax_order_total_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='city', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='state', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(default='00000', max_length=10),
        ),
    ]
