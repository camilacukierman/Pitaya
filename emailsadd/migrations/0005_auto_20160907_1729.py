# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0004_auto_20160907_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
