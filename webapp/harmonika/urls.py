from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'harmonika.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^o/', 'harmonika.web.views.organization', name='organization'),
    url(r'^students/', 'harmonika.web.views.students', name='students'),
    url(r'^student/(?P<slug>[\d\w_-]+)', 'harmonika.web.views.student', name='student'),
)
