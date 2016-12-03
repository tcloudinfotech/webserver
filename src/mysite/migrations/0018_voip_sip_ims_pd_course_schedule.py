# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_ltept_course_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='VOIP_SIP_IMS_PD_Course_Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=256, null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('duration', models.CharField(max_length=256, null=True, blank=True)),
                ('faculty', models.CharField(max_length=256, null=True, blank=True)),
                ('demo', models.URLField(max_length=256, null=True, blank=True)),
            ],
        ),
    ]
