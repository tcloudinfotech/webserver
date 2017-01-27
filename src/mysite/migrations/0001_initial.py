# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='base_database',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('batchtype', models.CharField(default=b'regular', max_length=24, choices=[(b'regular', b'REGULAR'), (b'weekend', b'WEEKEND'), (b'bootcamp', b'BOOTCAMP'), (b'online', b'ONLINE'), (b'fasttrack', b'FASTTRACK')])),
                ('duration', models.CharField(max_length=256, null=True, blank=True)),
                ('faculty', models.CharField(max_length=256, null=True, blank=True)),
                ('demo', models.URLField(max_length=256, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=256, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Popup_Window',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, null=True, blank=True)),
                ('phone', models.CharField(max_length=256, null=True, blank=True)),
                ('email', models.EmailField(max_length=24, null=True, blank=True)),
                ('course_name', models.ForeignKey(to='mysite.Course')),
            ],
        ),
        migrations.CreateModel(
            name='File_upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('files', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Ansibel_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Aws_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Chef_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Django_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Dockers_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Flask_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Git_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Iot_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Jenkins_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='L2_L3_Pd_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='L2_L3_Pt_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Ltepd_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Ltept_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Nagios_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Openstack_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Pandas_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Perl_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Python_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Ttcn3_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Voip_Sip_Ims_Pd_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.CreateModel(
            name='Voip_Sip_Ims_Pt_Course_Schedule',
            fields=[
                ('base_database_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='mysite.base_database')),
            ],
            options={
                'ordering': ['course_name', 'start_date', 'batchtype', 'duration', 'faculty', 'demo'],
            },
            bases=('mysite.base_database',),
        ),
        migrations.AddField(
            model_name='base_database',
            name='course_name',
            field=models.ForeignKey(to='mysite.Course'),
        ),
    ]
