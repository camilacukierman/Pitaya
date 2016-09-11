# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0009_auto_20160908_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booker',
            old_name='manager_massage',
            new_name='manager_message',
        ),
    ]
