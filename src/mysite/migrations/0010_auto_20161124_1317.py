# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_delete_django_subject_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python_Course_Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=256, null=True, blank=True)),
                ('start_date', models.DateTimeField(auto_now=True, null=True)),
                ('duration', models.CharField(max_length=256, null=True, blank=True)),
                ('faculty', models.CharField(max_length=256, null=True, blank=True)),
                ('demo', models.CharField(max_length=256, null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Course_Schedule',
            new_name='Django_Course_Schedule',
        ),
    ]
