# Generated by Django 4.1.2 on 2022-11-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('honeybee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog article', max_length=255),
        ),
    ]
