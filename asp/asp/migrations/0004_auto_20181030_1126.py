# Generated by Django 2.1.2 on 2018-10-30 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asp', '0003_auto_20181030_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]