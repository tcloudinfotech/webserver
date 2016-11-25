# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_course_popup_window_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Django_Subject_Details',
        ),
    ]
