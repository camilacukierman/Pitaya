# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('manager_name', models.CharField(null=True, max_length=50)),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(null=True, max_length=1000)),
                ('location', models.CharField(max_length=50)),
                ('to_time', models.DateTimeField()),
                ('from_time', models.DateTimeField()),
                ('date', models.DateTimeField()),
                ('manager_message', models.CharField(null=True, max_length=1000)),
                ('pic', models.ImageField(upload_to='pic_folder/', default='pic_folder/no-img.jpg')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('participants_name', models.CharField(null=True, max_length=50)),
                ('participants_email', models.EmailField(error_messages={'required': 'Please provide the email address.', 'unique': 'An account with this email exist.'}, max_length=254)),
                ('approved', models.BooleanField(default=False)),
                ('booker_id', models.ForeignKey(to='emailsadd.Booker')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('a1', models.IntegerField(default=0)),
                ('participant_ref', models.ForeignKey(to='emailsadd.Newsletter', default=1)),
            ],
        ),
    ]
