# Generated by Django 5.0.4 on 2024-04-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadCliente', '0009_membrofamilia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membrofamilia',
            name='sexo',
            field=models.CharField(choices=[('feminino', 'Feminino'), ('masculino', 'Masculino'), ('outros', 'Outros')], max_length=10),
        ),
    ]
