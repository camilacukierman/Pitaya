# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0002_booker_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booker',
            name='participants',
            field=models.EmailField(unique=True, error_messages={'unique': 'An account with this email exist.', 'required': 'Please provide your email address.'}, max_length=254),
        ),
    ]
