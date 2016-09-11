# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0012_auto_20160908_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='participants_email',
            field=models.EmailField(max_length=254, error_messages={'unique': 'An account with this email exist.', 'required': 'Please provide the email address.'}),
        ),
    ]
