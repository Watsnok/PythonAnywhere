# Generated by Django 2.1.1 on 2018-10-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaasApplication', '0012_auto_20181017_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='minprice',
            field=models.IntegerField(),
        ),
    ]
