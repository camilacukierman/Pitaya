# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0007_auto_20160907_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('participants_name', models.CharField(max_length=50)),
                ('participants_email', models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, unique=True, max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='booker',
            name='participants_email',
        ),
        migrations.RemoveField(
            model_name='booker',
            name='participants_number',
        ),
        migrations.AddField(
            model_name='booker',
            name='event_description',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='booker',
            name='manager_massage',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='booker',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booker',
            name='from_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booker',
            name='to_time',
            field=models.TimeField(),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='booker_id',
            field=models.ForeignKey(to='emailsadd.Booker'),
        ),
    ]
