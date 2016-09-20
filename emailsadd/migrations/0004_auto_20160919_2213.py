# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0003_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='answer_survey',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survey',
            name='booker_id',
            field=models.IntegerField(default=0),
        ),
    ]
