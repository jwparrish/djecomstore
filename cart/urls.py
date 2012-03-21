from django.conf.urls.defaults import *

urlpatterns = patterns('djecomstore.cart.views',
	(r'^$', 'show_cart', { 'template_name': 'cart/cart.html' }, 'show_cart'),
)