# Generated by Django 3.0.1 on 2020-05-16 04:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Nav1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('que', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelTable(
            name='question',
            table='Polls App',
        ),
    ]
