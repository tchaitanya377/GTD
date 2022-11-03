# Generated by Django 4.1.3 on 2022-11-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('complted', models.BooleanField()),
                ('property', models.CharField(blank=True, max_length=10)),
                ('ideas', models.TextField(blank=True)),
                ('goals', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
