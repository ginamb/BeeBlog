# Generated by Django 4.1.3 on 2022-11-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeybee', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(max_length=255)),
                ('honey', models.TextField(max_length=250)),
                ('time', models.DateTimeField(max_length=250)),
            ],
        ),
    ]
