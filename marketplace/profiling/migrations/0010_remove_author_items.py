# Generated by Django 3.2.16 on 2023-12-30 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0009_auto_20231230_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='items',
        ),
    ]