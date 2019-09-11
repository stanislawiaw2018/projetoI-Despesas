# Generated by Django 2.2.4 on 2019-09-11 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo_despesa', models.CharField(max_length=50)),
                ('forma_pagamento', models.CharField(choices=[('CA', 'cartao'), ('BO', 'boleto'), ('CRE', 'crediario'), ('DI', 'dinheiro')], default='CA', max_length=3)),
                ('descricao', models.TextField()),
                ('vencimento', models.DateField(blank=True, null=True)),
                ('quitado', models.BooleanField(default=True)),
            ],
        ),
    ]
