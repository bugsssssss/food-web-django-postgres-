# Generated by Django 4.1.6 on 2023-02-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_foodmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('phone', models.CharField(max_length=100, verbose_name='phone')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'Callback',
                'verbose_name_plural': 'Callbacks',
            },
        ),
    ]