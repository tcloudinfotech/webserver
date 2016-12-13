from django.db import models

# Create your models here.
class File_upload(models.Model):
    #upload_to='documents/%Y/%m/%d' argument
    files = models.FileField()

    def __unicode__(self):
        return unicode(self.files) or u''


class Course_Popup_Window(models.Model):
    name=models.CharField(max_length=256,null=True,blank=True)
    phone=models.CharField(max_length=256,null=True,blank=True)
    email=models.EmailField(max_length=24,null=True,blank=True)
    course=models.CharField(max_length=256,null=True,blank=True)
    




BATCH_CHOICES = (
    ('regular','REGULAR'),
    ('weekend', 'WEEKEND'),
    ('bootcamp','BOOTCAMP'),
    ('online','ONLINE'),
    ('fasttrack','FASTTRACK'),
)
# Course Schedule models

class base_database(models.Model):
    '''base model for course
    schedlue'''
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    batchtype=models.CharField(max_length=24, choices=BATCH_CHOICES, default='regular')
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)


#Cloud Course Schedule:

# Openstack Course Schedule:
class Openstack_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

# Amazon Webservices Course_Schedule
class Aws_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]



# Embeded Course Schedule:

# Internet of Things Course Schedule:
class Iot_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

# Devops Course Schedule:

#Ansibel Course Schedule:
class Ansibel_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#Dockers Course Schedule:
class Dockers_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]
#Chef Course Schedule:
class Chef_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#Nagios Course Schedule:
class Nagios_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#GIT Course Schedule:
class Git_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#Jenkins Course Schedule:
class Jenkins_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

# Scripting Course schedule:

class Python_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]


class Django_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]
 

class Flask_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]
    

class Pandas_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

class Perl_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]


class Ttcn3_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

# Telecom Course Schedule

# LTE Protocol Development Course Schedule:
class Ltepd_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]
    

# LTE Protocol Testing Course Schedule:
class Ltept_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]
# VOIP-SIP-IMS-Protocol Development:
class Voip_Sip_Ims_Pd_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#VOIP-SIP-IMS-Protocol Testing:
class Voip_Sip_Ims_Pt_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#Datacom Course Schedules:

#L2L3 Protocol Development Course Schedule:
class L2_L3_Pd_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

#L2 L3 Protocol Testing Course Schedule:
class L2_L3_Pt_Course_Schedule(base_database):
    class Meta:
        ordering = ["course_name","start_date","batchtype","duration","faculty","demo"]

# Contact Form Course model:

# class Course_Database_Mail(models.Model):
#     course=models.CharField(max_length=256,null=True,blank=True)

#     def __unicode__(self):
#         return self.course

class Course_Database_Mail(base_database):
    class Meta:
        ordering = ["course_name"]
