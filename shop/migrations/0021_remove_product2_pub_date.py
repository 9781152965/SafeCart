# Generated by Django 3.1.2 on 2020-10-28 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20201028_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product2',
            name='pub_date',
        ),
    ]
