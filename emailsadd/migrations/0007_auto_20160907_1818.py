# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0006_auto_20160907_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booker',
            old_name='participants',
            new_name='participants_email',
        ),
    ]
