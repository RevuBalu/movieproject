# Generated by Django 5.0 on 2024-02-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='online',
            name='id',
        ),
        migrations.AlterField(
            model_name='online',
            name='title',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]