# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_popup_window',
            name='course_name',
        ),
        migrations.AddField(
            model_name='course_popup_window',
            name='course',
            field=models.CharField(default=b'Python', max_length=256, null=True, blank=True),
        ),
    ]
