# Generated by Django 3.2.16 on 2024-01-08 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=50, verbose_name='slug'),
        ),
    ]
