from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

media_dirs = { 
    'css_dir': os.path.join(os.path.dirname(__file__), 'static/css').replace('\\', '/'), 
    'js_dir': os.path.join(os.path.dirname(__file__), 'static/js').replace('\\', '/'),   
    'img_dir': os.path.join(os.path.dirname(__file__), 'static/img').replace('\\', '/'), 
}



urlpatterns = patterns('',
    # Example:
    # (r'^dspillini/', include('dspillini.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dirs.get('css_dir')  }), 
    (r'^javascript/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dirs.get('js_dir') }), 
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': media_dirs.get('img_dir') }), 

	(r'^blog/', include('blog.urls')),
	(r'^events/', include('events.urls')),
	(r'^$', 'views.home'),
)
