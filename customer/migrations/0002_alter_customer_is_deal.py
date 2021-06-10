# Generated by Django 3.2.4 on 2021-06-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_deal',
            field=models.SmallIntegerField(choices=[(1, '成交'), (0, '未成交')], default=0, verbose_name='是否成交'),
        ),
    ]
