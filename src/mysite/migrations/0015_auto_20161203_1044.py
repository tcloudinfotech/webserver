# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20161203_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django_course_schedule',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='python_course_schedule',
            name='start_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
