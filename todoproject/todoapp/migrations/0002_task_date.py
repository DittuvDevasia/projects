# Generated by Django 3.2.14 on 2022-08-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-11-04'),
            preserve_default=False,
        ),
    ]
