from django.conf.urls.defaults import *
from djecomstore import settings

urlpatterns = patterns('djecomstore.checkout.views',
	(r'^$', 'show_checkout', {'template_name': 'checkout/checkout.html', 'SSL': settings.ENABLE_SSL}, 'checkout'),
	(r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html', 'SSL': settings.ENABLE_SSL}, 'checkout_receipt'),
)