# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20161210_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_database',
            name='batchtype',
            field=models.CharField(default=b'regular', max_length=24, choices=[(b'regular/online', b'REGULAR/ONLINE'), (b'weekend/online', b'WEEKEND/ONLINE'), (b'bootcamp', b'BOOTCAMP'), (b'online', b'ONLINE'), (b'fasttrack', b'FASTTRACK')]),
        ),
    ]
