"""
Definition of urls for proearthengine.
""" 
from django.conf.urls.static import static
from datetime import datetime
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import django.contrib.auth.views
from django.conf import settings
import app.forms
import app.views 
import app.models
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()
urlpatterns = [# Examples:
	url(r'^$', app.views.home, name='home'),
	url(r'^mail$', app.views.mail, name='mail'),
	url(r'^dataset$', app.views.dataset, name='dataset'),
	url(r'^compare$', app.views.compare, name='compare'),
	url(r'^about$', app.views.about, name='about'),
	url(r'^calc_data', app.views.calcdata, name='calc_data'),
	url(r'^calc_drought', app.views.cal_drought, name='calc_drought'),
	url(r'^download_data', app.views.download_data, name='download_data'),
	url(r'^chart_data', app.views.chart_data, name='chart_data'),
	url(r'^indices_compute', app.views.indices_compute, name='indices_compute'),
	url(r'^indices_download', app.views.indices_download, name='indices_download'),
	url(r'^map1', app.views.map1, name='map1'),	
	url(r'^map2', app.views.map2, name='map2'),
	url(r'^map3', app.views.map3, name='map3'),
	url(r'^map4', app.views.map4, name='map4'),
	url(r'^timeseries', app.views.timeseries, name='timeseries'),
   #Uncomment the admin/doc line below to enable admin documentation:
	 #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	 url(r'^admin/', include(admin.site.urls)),]


urlpatterns+=staticfiles_urlpatterns()

#urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)