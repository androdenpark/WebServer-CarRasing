from django.conf.urls import patterns, include, url
from django.contrib import admin
from racingCarApp.views import *
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'racingCar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^racingCar/getHomePage', huaPageRequest),
    url(r'^racingCar/hua_dataPost', huaDataPost),
    url(r'^racingCarApp/static/(?P<path>.*)', "django.views.static.serve",
        {'document_root':"/var/www/racingCar/racingCar/racingCarApp/static"}),

)
