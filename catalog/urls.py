from django.conf.urls.defaults import *
from djecomstore.catalog.views import *

urlpatterns = patterns('djecomstore.catalog.views',
	(r'^$', 'index', { 'template_name': 'catalog/index.html'}, 'catalog_home'),
	(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', { 'template_name': 'catalog/category.html'}, 'catalog_category'),
	(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', { 'template_name': 'catalog/product.html'}, 'catalog_product'),
	(r'^review/product/add/$', 'add_review'),
	(r'^tag/product/add/$', 'add_tag'),
	(r'^tag_cloud/$', 'tag_cloud', {'template_name': 'catalog/tag_cloud.html'}, 'tag_cloud'),
	(r'^tag/(?P<tag>[-\w]+)/$', 'tag', {'template_name': 'catalog/tag.html'}, 'tag'),
	
	(r'^json/', get_json_products),
)