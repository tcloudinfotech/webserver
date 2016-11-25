from django.db import models

# Create your models here.


# Course Schedule models
class Django_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateField(auto_now=True,null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.CharField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return self.course_name


class Python_Course_Schedule(models.Model):
    course_name=models.CharField(max_length=256,null=True,blank=True)
    start_date=models.DateTimeField(auto_now=True,null=True,blank=True)
    duration=models.CharField(max_length=256,null=True,blank=True)
    faculty=models.CharField(max_length=256,null=True,blank=True)
    demo = models.CharField(max_length=256,null=True,blank=True)

    def __unicode__(self):
        return self.course_name



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


