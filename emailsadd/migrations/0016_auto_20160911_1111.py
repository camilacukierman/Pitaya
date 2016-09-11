# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0015_booker_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='manager_name',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
