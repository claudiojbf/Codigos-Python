# Generated by Django 4.0.6 on 2022-08-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_trasferencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contadortrasferencia',
            name='valor_ultimas',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
