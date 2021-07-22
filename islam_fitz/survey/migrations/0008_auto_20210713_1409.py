# Generated by Django 3.1.12 on 2021-07-13 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20210713_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='clientanswerlist',
            name='client_answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='survey.answer'),
        ),
        migrations.AlterUniqueTogether(
            name='clientanswerlist',
            unique_together={('client', 'client_answer')},
        ),
    ]