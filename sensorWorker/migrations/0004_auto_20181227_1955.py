# Generated by Django 2.1.2 on 2018-12-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorWorker', '0003_auto_20181227_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='horaEntrada',
            field=models.TimeField(auto_now_add=True),
        ),
    ]