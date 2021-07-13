# Generated by Django 3.1.12 on 2021-07-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/about_us/%y/%m/%d')),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='BeforeAndAfter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='photos/before_and_after/%y/%m/%d')),
                ('feature', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='photos/logo/%y/%m/%d')),
                ('intro_image', models.ImageField(upload_to='photos/home/%y/%m/%d')),
                ('intro_text', models.CharField(max_length=400)),
                ('about_us_image', models.ImageField(upload_to='photos/home/%y/%m/%d')),
                ('about_us_text', models.CharField(max_length=400)),
            ],
        ),
    ]
