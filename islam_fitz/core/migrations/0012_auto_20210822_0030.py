# Generated by Django 3.1.12 on 2021-08-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210819_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beforeandafter',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
