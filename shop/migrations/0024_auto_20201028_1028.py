# Generated by Django 3.1.2 on 2020-10-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20201028_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product2',
            name='pro_image',
            field=models.ImageField(default='', upload_to='shop2/images2'),
        ),
    ]
