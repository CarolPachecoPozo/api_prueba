# Generated by Django 5.1.3 on 2024-12-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humedad', models.IntegerField()),
                ('temperatura', models.IntegerField()),
            ],
        ),
    ]
