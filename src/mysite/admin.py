from django.contrib import admin
from mysite.models import *

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'start_date','duration','faculty','demo')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course','phone','email')

    class Meta:
        model = Course_Popup_Window()


admin.site.register(Course)
admin.site.register(File_upload)
admin.site.register(Course_Popup_Window,CourseAdmin)
admin.site.register(Django_Course_Schedule,PersonAdmin)
admin.site.register(Python_Course_Schedule,PersonAdmin)
admin.site.register(Flask_Course_Schedule,PersonAdmin)
admin.site.register(Perl_Course_Schedule,PersonAdmin)
admin.site.register(Pandas_Course_Schedule,PersonAdmin)
admin.site.register(Ttcn3_Course_Schedule,PersonAdmin)
admin.site.register(Ltepd_Course_Schedule,PersonAdmin)
admin.site.register(Ltept_Course_Schedule,PersonAdmin)
admin.site.register(Voip_Sip_Ims_Pd_Course_Schedule,PersonAdmin)
admin.site.register(Voip_Sip_Ims_Pt_Course_Schedule,PersonAdmin)
admin.site.register(L2_L3_Pd_Course_Schedule,PersonAdmin)
admin.site.register(L2_L3_Pt_Course_Schedule,PersonAdmin)
admin.site.register(Openstack_Course_Schedule,PersonAdmin)
admin.site.register(Aws_Course_Schedule,PersonAdmin)
admin.site.register(Iot_Course_Schedule,PersonAdmin)
admin.site.register(Ansibel_Course_Schedule,PersonAdmin)
admin.site.register(Dockers_Course_Schedule,PersonAdmin)
admin.site.register(Chef_Course_Schedule,PersonAdmin)
admin.site.register(Nagios_Course_Schedule,PersonAdmin)
admin.site.register(Git_Course_Schedule,PersonAdmin)
admin.site.register(Jenkins_Course_Schedule,PersonAdmin)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('topic','content')

# admin.site.register(Django_Subject_Details,CourseAdmin)
