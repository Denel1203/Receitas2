# Generated by Django 4.1.3 on 2022-12-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0006_alter_receitas_nome_receita_alter_receitas_notas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='Notas',
            field=models.TextField(max_length=200),
        ),
    ]
