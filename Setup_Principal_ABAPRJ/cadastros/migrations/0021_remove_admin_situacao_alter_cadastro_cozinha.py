# Generated by Django 5.1a1 on 2024-05-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0020_admin_situacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="situacao",
        ),
        migrations.AlterField(
            model_name="cadastro",
            name="cozinha",
            field=models.IntegerField(verbose_name="QuantidAade de cozinha(s)"),
        ),
    ]