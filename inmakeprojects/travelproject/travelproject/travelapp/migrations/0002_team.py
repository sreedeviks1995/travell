# Generated by Django 3.1.7 on 2021-03-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_t', models.CharField(max_length=250)),
                ('img_t', models.ImageField(upload_to='pictures')),
                ('desc_t', models.TextField()),
            ],
        ),
    ]
