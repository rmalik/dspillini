from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^alumni/carillon/$', 'views.carillon_archive'),
	(r'^students/scholarship/$', 'views.scholarship'),
	(r'^students/costs/$', 'views.costs'),
	(r'^students/join/$', 'views.join_us'),
	(r'^parents/concerns/$', 'views.concerns'),
	(r'^parents/visit/$', 'views.schedule_visit'),
	(r'^$', 'views.home'),
)