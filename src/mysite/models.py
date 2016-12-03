from django.db import models

# Create your models here.
class File_upload(models.Model):
    #upload_to='documents/%Y/%m/%d' argument
    files = models.FileField()

    def __unicode__(self):
        return unicode(self.files) or u''


class Course_Popup_Window(models.Model):
    name=models.CharField(max_length=256,null=True,blank=True)
    course=models.CharField(max_length=256,null=True,blank=True)
    phone=models.CharField(max_length=256,null=True,blank=True)

class Course_Database_Mail(models.Model):
    course=models.CharField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return self.course


# Course Schedule models

# Scripting Course schedule:

class Django_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)


class Python_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)



# Telecom Course Schedule

# LTE Protocol Development Course Schedule:
class Ltepd_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)


# LTE Protocol Testing Course Schedule:
class Ltept_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)

# VOIP-SIP-IMS-Protocol Development:
class Voip_Sip_Ims_Pd_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)

#VOIP-SIP-IMS-Protocol Testing:
class Voip_Sip_Ims_Pt_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)


#Datacom Course Schedules:

#L2L3 Protocol Development Course Schedule:
class L2_L3_Pd_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)

#L2 L3 Protocol Testing Course Schedule:
class L2_L3_Pt_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.URLField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s,%s' %(self.course_name,self.start_date,self.duration,
            self.faculty,self.demo)





