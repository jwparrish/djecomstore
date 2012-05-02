from django.conf.urls.defaults import *

urlpatterns = patterns('djecomstore.billing.views',
	(r'^add_card/$', 'add_card'),
)