# Generated by Django 4.0.6 on 2022-08-03 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_conta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='saldo',
            field=models.FloatField(),
        ),
    ]
