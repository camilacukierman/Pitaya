# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0005_auto_20160907_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booker',
            old_name='time',
            new_name='from_time',
        ),
        migrations.RemoveField(
            model_name='booker',
            name='duration',
        ),
        migrations.AddField(
            model_name='booker',
            name='to_time',
            field=models.TimeField(null=True),
        ),
    ]
