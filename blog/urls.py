from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\w-]+)/$', 'entry_detail'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month'),
    (r'^(?P<year>\d{4})/$', 'archive_year'),
    (r'^$', 'archive_index'),
	(r'^create/$', 'create'),
)