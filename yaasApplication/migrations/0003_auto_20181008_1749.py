# Generated by Django 2.1.1 on 2018-10-08 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yaasApplication', '0002_auto_20180922_1958'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]