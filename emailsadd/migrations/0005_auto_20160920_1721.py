# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0004_auto_20160919_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='a2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='a3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survey',
            name='a4',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
