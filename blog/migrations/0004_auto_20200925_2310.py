# Generated by Django 3.1.1 on 2020-09-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200925_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tittle',
            field=models.CharField(max_length=500),
        ),
    ]
