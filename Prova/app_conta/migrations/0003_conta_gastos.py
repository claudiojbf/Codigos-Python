# Generated by Django 4.0.6 on 2022-08-03 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_conta', '0002_alter_conta_saldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='gastos',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]