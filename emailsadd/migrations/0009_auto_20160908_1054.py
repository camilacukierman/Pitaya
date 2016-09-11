# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0008_auto_20160908_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='participants_email',
            field=models.EmailField(error_messages={'required': 'Please provide the email address.', 'unique': 'An account with this email exist.'}, unique=True, max_length=254),
        ),
    ]
