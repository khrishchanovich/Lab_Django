# Generated by Django 3.1.5 on 2023-06-03 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'ordering': ['id'], 'verbose_name': 'Контракт', 'verbose_name_plural': 'Контракты'},
        ),
        migrations.AlterModelOptions(
            name='insuranceagent',
            options={'ordering': ['last_name'], 'verbose_name': 'Агент', 'verbose_name_plural': 'Агенты'},
        ),
        migrations.AlterModelOptions(
            name='insuranceobjects',
            options={'ordering': ['name'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.RemoveField(
            model_name='contract',
            name='slug',
        ),
    ]
