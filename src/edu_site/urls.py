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
    url(r'^embeded/','mysite.views.embeded',name='embeded'),
    url(r'^devops/','mysite.views.devops',name='devops'),
    url(r'^cloud/','mysite.views.cloud',name='cloud'),
    url(r'^info/','mysite.views.my_fun',name='info'),
    # Main tab of telecome and relative subtags.
    url(r'^Telecom/','mysite.views.telecom',name='telecom'),
    url(r'^LTEProtocolDevelopment/','mysite.views.LTEPD',name='ltepd'),
    url(r'^LTEProtocolTesting/','mysite.views.LTEPT',name='ltept'),
    url(r'^VOIPSipImsProtocolDevelopment/','mysite.views.VOIP_SIP_IMS_PD',name='voippd'),
    url(r'^VOIPSipImsProtocolTesting/','mysite.views.VOIP_SIP_IMS_PT',name='voippt'),
    # Main tab of scripting and relative subtags.
    url(r'^Scripting/','mysite.views.scripting',name='scripting'),
    url(r'^PythonProgramming/','mysite.views.python',name='python'),
    url(r'^DjangoFramework/','mysite.views.django',name='django'),
    url(r'^pandasDataAnalysis/','mysite.views.pandas',name='pandas'),
    url(r'^PerlProgramming/','mysite.views.perl',name='perl'),
    url(r'^ttcn3/','mysite.views.ttcn3',name='ttcn3'),

    # services
    url(r'^services/$','mysite.views.services',name='services'),

    
    

]
