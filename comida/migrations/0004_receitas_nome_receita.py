# Generated by Django 4.1.3 on 2022-12-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0003_remove_receitas_introducao'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='Nome_Receita',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
