# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20161210_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_popup_window',
            name='email',
            field=models.EmailField(max_length=24, null=True, blank=True),
        ),
    ]
