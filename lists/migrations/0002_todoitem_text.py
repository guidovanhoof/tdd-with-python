# Generated by Django 4.1.5 on 2023-01-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
