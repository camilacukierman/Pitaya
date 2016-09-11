# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0011_remove_booker_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='participants_name',
            field=models.CharField(null=True, max_length=50),
        ),
    ]
