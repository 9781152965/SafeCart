# Generated by Django 3.1.1 on 2020-10-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
