from django.conf.urls.defaults import *

urlpatterns = patterns('djecomstore.search.views',
	(r'^results/$', 'results', {'template_name': 'search/results.html'}, 'search_results'),
)