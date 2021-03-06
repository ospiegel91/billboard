# Generated by Django 2.1.5 on 2019-01-11 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=600)),
                ('author', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Message',
            },
        ),
    ]
