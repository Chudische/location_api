# Generated by Django 3.2.1 on 2021-06-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_place_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255, verbose_name='Область')),
                ('area', models.CharField(max_length=255, verbose_name='Район')),
                ('place', models.CharField(max_length=255, verbose_name='Населенный пункт')),
                ('post_index', models.CharField(max_length=5, verbose_name='Индекс отделения')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('houses', models.CharField(max_length=2000, verbose_name='Дома')),
            ],
            options={
                'verbose_name': 'База данных почты',
                'verbose_name_plural': 'База данных почты',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='is_location',
            field=models.BooleanField(default=True, verbose_name='Это НП?'),
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('О', 'ОБЛАСТЬ '), ('Р', 'РАЙОН '), ('М', 'м. '), ('Т', 'смт. '), ('С', 'с. '), ('Щ', 'с. ')], max_length=1, verbose_name='Категория'),
        ),
    ]
