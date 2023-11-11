# Generated by Django 4.1 on 2023-11-09 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Freezer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название лаборатории')),
                ('head_lab', models.CharField(default='', max_length=50, verbose_name='Заведующий лабораторий')),
                ('test_field', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
            ],
            options={
                'verbose_name': 'Лаборатория',
                'verbose_name_plural': 'Лаборатории',
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('freezer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobank.freezer')),
            ],
        ),
        migrations.CreateModel(
            name='SampleLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('count_samples', models.IntegerField(default=0)),
                ('count_rows', models.IntegerField(default=0)),
                ('count_col', models.IntegerField(default=0)),
                ('state_location', models.CharField(default='free', max_length=10)),
                ('sample_id', models.IntegerField(default=-1)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobank.box')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название образца')),
                ('test_field', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('description', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('laboratory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='biobank.laboratory')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.AddField(
            model_name='box',
            name='shelf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobank.shelf'),
        ),
        migrations.CreateModel(
            name='Biospecimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Название образца')),
                ('test_field', models.CharField(default='', max_length=250, verbose_name='Тестовое поле')),
                ('date', models.DateTimeField(verbose_name='Дата получения')),
                ('file_name', models.CharField(max_length=50, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='upldfile/')),
                ('name_storage_sample', models.CharField(default='', max_length=100, verbose_name='Место хранения образца в хранилище')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobank.samplelocation')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biobank.project')),
            ],
            options={
                'verbose_name': 'Биологический образец',
                'verbose_name_plural': 'Биологические образцы',
            },
        ),
    ]