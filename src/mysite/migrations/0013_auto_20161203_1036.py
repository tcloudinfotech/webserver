# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20161203_1033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LTE_PD_Course_Schedule',
            new_name='Ltepd_Course_Schedule',
        ),
    ]
