# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0002_auto_20160917_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('a1', models.IntegerField(default=0)),
                ('participant_ref', models.ForeignKey(default=1, to='emailsadd.Newsletter')),
            ],
        ),
    ]
