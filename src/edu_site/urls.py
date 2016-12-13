from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'edu_site.views.home', name='home'),
    # url(r'^edu_site/', include('edu_site.urls')),
    url(r'^some_view/', 'mysite.views.some_view',name='some_view'),
    url(r'^Pop_Up_view/', 'mysite.views.Pop_Up_view',name='Pop_Up_view'),
    url(r'^Contact_View_Popup/', 'mysite.views.Contact_View_Popup',name='Contact_View_Popup'),
    url(r'^course_index/', 'mysite.views.course_index',name='course_index'),
    url(r'^courses/','mysite.views.courses',name='courses'),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^$','mysite.views.myhome', name='home'),
    
    url(r'^contact/','mysite.views.Contact_View',name='contact'),
    url(r'^aboutus/','mysite.views.aboutus',name='aboutus'),
    # course tabs
    url(r'^datacom/','mysite.views.datacom',name='datacom'),
    
    
    
    url(r'^info/','mysite.views.my_fun',name='info'),
    # Main tab of telecome and relative subtags.
    url(r'^Telecom/','mysite.views.telecom',name='telecom'),
    url(r'^LTE-Protocol-Development/','mysite.views.LTEPD',name='ltepd'),
    url(r'^LTE-Protocol-Testing/','mysite.views.LTEPT',name='ltept'),
    url(r'^VOIP-SIP-IMS-Protocol-Development/','mysite.views.VOIP_SIP_IMS_PD',name='voippd'),
    url(r'^VOIP-SIP-IMS-Protocol-Testing/','mysite.views.VOIP_SIP_IMS_PT',name='voippt'),

    #main tab of datacom and relative subtags
    url(r'^L2&L3-Protocol-Development','mysite.views.l2l3dev',name='l2l3dev'),
    url(r'^L2&L3-Protocol-Testing','mysite.views.l2l3test',name='l2l3test'),


    # Main tab of scripting and relative subtags.
    url(r'^Scripting/','mysite.views.scripting',name='scripting'),
    url(r'^Python-Programming/','mysite.views.python',name='python'),
    url(r'^Django-Web_Framework/','mysite.views.django',name='django'),
    url(r'^Flask-Web_Framework/','mysite.views.flask',name='flask'),
    url(r'^Pandas-Data-Analysis/','mysite.views.pandas',name='pandas'),
    url(r'^Perl-Programming/','mysite.views.perl',name='perl'),
    url(r'^Testing&Test-Control-Notation_3/','mysite.views.ttcn3',name='ttcn3'),

    # main tab for cloud and relative subtags
    url(r'^Cloud/','mysite.views.cloud',name='cloud'),
    url(r'^Openstack/','mysite.views.openstack',name='openstack'),
    url(r'^Amazon-Web-Services/','mysite.views.aws',name='aws'),


    # Main tab for cloud and relative subtags
    url(r'^embeded/','mysite.views.embeded',name='embeded'),
    url(r'^Internet-of-Things/','mysite.views.iot',name='iot'),

    # Main urls for devops and relative subtags
    url(r'^Devops/','mysite.views.devops',name='devops'),
    url(r'^Ansibel/','mysite.views.ansibel',name='ansibel'),
    url(r'^Dockers/','mysite.views.dockers',name='dockers'),
    url(r'^Chef/','mysite.views.chef',name='chef'),
    url(r'^Nagios/','mysite.views.nagios',name='nagios'),
    url(r'^GIT/','mysite.views.git',name='git'),
    url(r'^Jenkins/','mysite.views.jenkins',name='jenkins'),
    


    # services
    #url(r'^services/','mysite.views.services',name='services'),
    url(r'^products/','mysite.views.products',name='products'),
    url(r'^services/','mysite.views.services',name='services'),
    
    # Other Schedules for Scripting:

    url(r'^python_schedules/','mysite.views.python_schedules',name='python_schedules'),
    url(r'^django_schedules/','mysite.views.django_schedules',name='django_schedules'),
    url(r'^flask_schedules/','mysite.views.flask_schedules',name='flask_schedules'),
    url(r'^pandas_schedules/','mysite.views.pandas_schedules',name='pandas_schedules'),
    url(r'^perl_schedules/','mysite.views.perl_schedules',name='perl_schedules'),
    url(r'^ttcn3_schedules/','mysite.views.ttcn3_schedules',name='ttcn3_schedules'),

    # Other Schedules for Telecom:

    url(r'^ltepd_schedules/','mysite.views.ltepd_schedules',name='ltepd_schedules'),
    url(r'^ltept_schedules/','mysite.views.ltept_schedules',name='ltept_schedules'),
    url(r'^voipsipimspd_schedules/','mysite.views.voipsipimspd_schedules',
        name='voipsipimspd_schedules'),
    url(r'^voipsipimspt_schedules/','mysite.views.voipsipimspt_schedules',
        name='voipsipimspt_schedules'),
    
    # Other Schedules for Datacom:

    url(r'^l2l3pd_schedules/','mysite.views.l2l3pd_schedules',name='l2l3pd_schedules'),
    url(r'^l2l3pt_schedules/','mysite.views.l2l3pt_schedules',name='l2l3pt_schedules'),

    # Other Schedules for Embeded:

    url(r'^IOT_schedules/','mysite.views.IOT_schedules',name='IOT_schedules'),

    # Other Schedules for Devops

    url(r'^ansibel_schedules/','mysite.views.ansibel_schedules',name='ansibel_schedules'),
    url(r'^dockers_schedules/','mysite.views.dockers_schedules',name='dockers_schedules'),
    url(r'^chef_schedules/','mysite.views.chef_schedules',name='chef_schedules'),
    url(r'^nagios_schedules/','mysite.views.nagios_schedules',name='nagios_schedules'),
    url(r'^git_schedules/','mysite.views.ttcn3_schedules',name='ttcn3_schedules'),
    url(r'^GIT_schedules/','mysite.views.GIT_schedules',name='GIT_schedules'),
    url(r'^jenkins_schedules/','mysite.views.jenkins_schedules',name='jenkins_schedules'),

    # Other Schedules for Cloud:

    url(r'^openstack_schedules/','mysite.views.openstack_schedules',name='openstack_schedules'),
    url(r'^AWS_schedules/','mysite.views.AWS_schedules',name='AWS_schedules'),







    
    

]
