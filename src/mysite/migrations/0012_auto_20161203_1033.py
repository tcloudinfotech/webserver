# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_ltepd_course_schedule'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LTEPD_Course_Schedule',
            new_name='LTE_PD_Course_Schedule',
        ),
    ]
