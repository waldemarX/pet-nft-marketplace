# Generated by Django 3.2.16 on 2023-12-30 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0005_auto_20231230_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='profiling.author', unique=True, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='profiling.author', unique=True, verbose_name='owner'),
        ),
    ]