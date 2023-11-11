# Generated by Django 4.1 on 2023-11-09 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название образца')),
                ('test_field', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('description', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('laboratory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='laboratory.laboratory')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
