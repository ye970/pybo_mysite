# Generated by Django 3.1.3 on 2021-10-01 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='contetn',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
