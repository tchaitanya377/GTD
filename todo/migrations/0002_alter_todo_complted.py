# Generated by Django 4.1.3 on 2022-11-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complted',
            field=models.BooleanField(default=False),
        ),
    ]
