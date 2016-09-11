# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('company_name', models.CharField(max_length=50)),
                ('manager_name', models.CharField(max_length=50)),
                ('event_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('participants_number', models.IntegerField(null=True)),
            ],
        ),
    ]
