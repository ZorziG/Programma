# Generated by Django 4.0.6 on 2022-08-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0002_alter_anagrafica_abi_alter_anagrafica_cab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='cellurare',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='anagrafica',
            name='telefono',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
