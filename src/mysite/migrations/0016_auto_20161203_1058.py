# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20161203_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_course_schedule',
            name='demo',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ltepd_course_schedule',
            name='demo',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='python_course_schedule',
            name='demo',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
    ]
