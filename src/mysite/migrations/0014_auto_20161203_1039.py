# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20161203_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltepd_course_schedule',
            name='start_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
