from django.conf.urls.defaults import *
from djecomstore.marketing.sitemap import SITEMAPS

urlpatterns = patterns('djecomstore.marketing.views',
	(r'^robots\.txt$', 'robots'),
)

urlpatterns += patterns('',
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': SITEMAPS }),
)