# Generated by Django 4.0.1 on 2022-02-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('issues', models.CharField(default='No Issues', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
