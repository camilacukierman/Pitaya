# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='participant_ref',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
