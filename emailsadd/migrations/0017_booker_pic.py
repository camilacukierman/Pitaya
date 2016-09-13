# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailsadd', '0016_auto_20160911_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='booker',
            name='pic',
            field=models.ImageField(default=b'pic_folder/no-img.jpg', upload_to=b'pic_folder/'),
        ),
    ]
