from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^blog/', include('blog.urls'))
)