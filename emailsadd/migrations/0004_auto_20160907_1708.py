# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0003_auto_20160904_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
