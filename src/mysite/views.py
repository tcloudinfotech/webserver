import os
from django.shortcuts import render,redirect,render_to_response,RequestContext,HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactEmailForm,ContactEmailForm_Popup
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from mysite.models import *
from reportlab.pdfgen import canvas
from wsgiref.util import FileWrapper
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from mysite.forms import Pop_Up_Form


#@login_required(login_url="/accounts/login/")
def some_view(request):
    # file = open(r'C:/Python27/Scripts/src/documents/djangobook.pdf', "w+b")
    #path = os.path(r'C:/Python27/Scripts/src/documents/djangobook.pdf')
    try:
        return FileResponse(open(r'C:/Python27/Scripts/src/documents/CSS3.pdf', 'rb'),
         content_type='application/pdf')
    except :
        raise Http404()


def my_fun(request):
    return HttpResponse("hello Tcloud")



# COUSES PAGE POP UP - For database
# The form data is getting populated in the database.

def Pop_Up_view(request):
    form = Pop_Up_Form(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data['name']
        phone=form.cleaned_data['phone']
        email=form.cleaned_data['email']
        # print '******************************************',name
        course=form.cleaned_data['course']
        Course_Popup_Window.objects.get_or_create(
            name=name,
            phone=phone,
            email=email,
            course=course,
        )
        return HttpResponseRedirect('')

# COURSES PAGE POPUP FORM - for sending mails
# This form is for sending the mail for us.

def Contact_View_Popup(request):
    form =ContactEmailForm_Popup(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get('name')
        course=form.cleaned_data.get('course')
        email=form.cleaned_data.get('email')
        phone=form.cleaned_data.get('phone')
        contact_message = 'Email: %s\n Name:%s\n Course: %s\n Phone:%s\n' %(email,name,course,phone)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'info@tcloudtech.com']
        subject = '{} - {} - {}'.format(name,course,phone)
        send_mail (subject,
                   contact_message,
                   to_email,
                   fail_silently=False)
        return redirect('/home/')
    context={'form':form}
    return render(request,'Telecome/LTEPD.html',context)


 # ABOUT PAGE CONTACT FORM

def Contact_View(request):
    form =ContactEmailForm(request.POST or None)

    if form.is_valid():
        email=form.cleaned_data.get('email')
        name=form.cleaned_data.get('name')
        phone=form.cleaned_data.get('phone')
        course=form.cleaned_data.get('course')
        message=form.cleaned_data.get('message')
        subject='{} - {}'.format(name,course)
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email, 'info@tcloudtech.com']
        contact_message='Email: %s\n Name:%s\n Course: %s\n Phone:%s\n Message: %s  ' %(email,name,course,phone,message)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        print contact_message

        return redirect('/contact/')

    context={'form':form}
    return render(request,'Bootup/contact.html',context)





def course_index(request):
    context={}
    return render(request,'Bootup/my_course.html',context)


def myhome(request):
    context={}
    return render(request,'Bootup/home.html',context)


def courses(request):
    context={}
    return render(request,'Bootup/course.html',context)


def aboutus(request):
	context={}
	return render(request,'Bootup/about-us.html',context)

# services page
def services(request):
    context = {}
    return render(request,'services/services1.html',context)

def products(request):
    context = {}
    return render(request,'products/products.html',context)


def embeded(request):
    context={}
    return render(request,'courses/embeded.html',context)


# Main page for Telecom

def telecom(request):
    context={}
    return render(request,'courses/telecom.html',context)

# Details for Telecome course content subtabs - read more

def LTEPD(request):
    property = [Ltepd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/LTEPD.html',context,
        context_instance=RequestContext(request))



def LTEPT(request):
    property = [Ltept_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/LTEPT.html',context)


def VOIP_SIP_IMS_PD(request):
    property = [Voip_Sip_Ims_Pd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/VOIP_SIP_IMS_PD.html',context)


def VOIP_SIP_IMS_PT(request):
    property = [Voip_Sip_Ims_Pt_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/VOIP_SIP_IMS_PT.html',context)


#Main Page for Datacom

def datacom(request):
    context={}
    return render(request,'courses/datacom.html',context)

# Details for Datacom courses content subtabs - read more

def l2l3dev(request):
    property= [L2_L3_Pd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Datacom/L2_L3_Dev.html',context)

def l2l3test(request):
    property = [L2_L3_Pt_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request, 'courses/Datacom/L2_L3_Test.html',context,
        context_instance=RequestContext(request))




# Main page for scripting

def scripting(request):
    context={}
    return render(request,'courses/scripting.html',context)

# Detail for scripting course Content subtabs - read more.

def python(request):
    property = [Python_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/scripting/python.html',context, context_instance=RequestContext(request))

def pandas(request):
    context={}
    return render(request,'courses/scripting/pandas.html',context)

def perl(request):
    context={}
    return render(request,'courses/scripting/perl.html',context)

def ttcn3(request):
    context={}
    return render(request,'courses/scripting/ttcn3.html',context)

def flask(request):
    context={}
    return render(request,'courses/scripting/flask.html',context)

def django(request):
    property = [Django_Course_Schedule.objects.last()]
    #property1 = Django_Subject_Details.objects.order_by('topic')
    itemin = {'property': property}
    return render_to_response('courses/scripting/django.html', itemin, context_instance=RequestContext(request))



# main views for cloud

def cloud(request):
    context={}
    return render(request,'courses/cloud.html',context)

#Detiled view for openstack and readmore
def openstack(request):
    property = [Openstack_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Cloud/Openstack.html',context)

#Detailed view for Amazon Web Services and readmore
def aws(request):
    property = [Aws_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Cloud/AWS.html',context)

# main Page for Embeded

def embeded(request):
    context={}
    return render(request,'courses/embeded.html',context)

# Detailed page for Internet of Things:
def iot(request):
    property = [Iot_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Embeded/IOT.html',context)



# main Page for Devops

def devops(request):
    context={}
    return render(request,'courses/devops.html',context)

# Detailed page for Ansibel:
def ansibel(request):
    property = [Ansibel_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Ansibel.html',context)

# Detailed page for Dockers:
def dockers(request):
    property = [Dockers_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Dockers.html',context)

# Detailed page for Chef:
def chef(request):
    property = [Chef_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Chef.html',context)

# Detailed page for Chef:
def nagios(request):
    property = [Nagios_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Nagios.html',context)

# Detailed page for GIT:
def git(request):
    property = [Git_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Git.html',context)

# Detailed page for Jenkins:
def jenkins(request):
    property = [Jenkins_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Jenkins.html',context)



# Other Schedules for Scripting:

def python_schedules(request):
    property = Python_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/python_schedules.html',context)

def django_schedules(request):
    property = Django_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/django_schedules.html',context)

def flask_schedules(request):
    property = Flask_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/flask_schedules.html',context)

def pandas_schedules(request):
    property = Pandas_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/pandas_schedules.html',context)

def perl_schedules(request):
    property = Perl_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/perl_schedules.html',context)

def ttcn3_schedules(request):
    property = Ttcn3_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/scripting/TTCN3_schedules.html',context)

# Telecom Other Schedules:

def ltepd_schedules(request):
    property = Ltepd_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/telecom/LTEPD_schedules.html',context)

def ltept_schedules(request):
    property = Ltept_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/telecom/LTEPT_schedules.html',context)

def voipsipimspd_schedules(request):
    property = Voip_Sip_Ims_Pd_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/telecom/VOIPSIPIMSPD_schedules.html',context)

def voipsipimspt_schedules(request):
    property = Voip_Sip_Ims_Pt_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/telecom/VOIPSIPIMSPT_schedules.html',context)

# Datacom Other Schedules

def l2l3pd_schedules(request):
    property = L2_L3_Pd_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/datacom/L2L3PD_schedules.html',context)

def l2l3pt_schedules(request):
    property = L2_L3_Pt_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/datacom/L2L3PT_schedules.html',context)

# Embeded Other Schedules

def IOT_schedules(request):
    property = Iot_Course_Schedule.objects.all().order_by('-id')[:3]
    context = {'property': property}
    return render(request,'courses/schedules/embeded/IOT_schedules.html',context)

# Deveops Other Schedules:

def ansibel_schedules(request):
    property = Ansibel_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/ansibel_schedules.html',context)

def dockers_schedules(request):
    property = Dockers_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/dockers_schedules.html',context)

def chef_schedules(request):
    property = Chef_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/chef_schedules.html',context)

def nagios_schedules(request):
    property = Nagios_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/nagios_schedules.html',context)

def GIT_schedules(request):
    property = Git_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/GIT_schedules.html',context)

def jenkins_schedules(request):
    property = Jenkins_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/devops/jenkins_schedules.html',context)

# Cloud other Schedules:

def AWS_schedules(request):
    property = Aws_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/cloud/AWS_schedules.html',context)

def openstack_schedules(request):
    property = Openstack_Course_Schedule.objects.all().order_by('-id')[:3]
    context={'property': property}
    return render(request,'courses/schedules/cloud/openstack_schedules.html',context)
