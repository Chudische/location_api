# Generated by Django 3.2.1 on 2021-05-25 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='raiting',
            new_name='rating',
        ),
    ]
