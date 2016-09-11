# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booker',
            name='participants',
            field=models.EmailField(default='tzvi@bla.bla', max_length=254, error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, unique=True),
        ),
    ]
