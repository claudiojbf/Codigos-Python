# Generated by Django 4.0.6 on 2022-08-03 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_conta', '0004_remove_conta_gastos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_conta.conta')),
            ],
        ),
    ]
