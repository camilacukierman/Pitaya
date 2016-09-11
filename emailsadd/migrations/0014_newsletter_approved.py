# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0013_auto_20160908_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
