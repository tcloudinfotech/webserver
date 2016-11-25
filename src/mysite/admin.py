from django.contrib import admin
from mysite.models import *

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'start_date','duration','faculty','demo')


admin.site.register(File_upload)
admin.site.register(Course_Database_Mail)
admin.site.register(Django_Course_Schedule,PersonAdmin)
admin.site.register(Python_Course_Schedule,PersonAdmin)

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('topic','content')

# admin.site.register(Django_Subject_Details,CourseAdmin)