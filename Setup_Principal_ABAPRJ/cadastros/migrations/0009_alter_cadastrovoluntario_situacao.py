# Generated by Django 5.0.4 on 2024-05-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0008_alter_cadastrovoluntario_situacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastrovoluntario",
            name="situacao",
            field=models.CharField(
                default="Candidato", max_length=100, verbose_name="Situação"
            ),
        ),
    ]
