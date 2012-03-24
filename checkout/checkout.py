from djecomstore.checkout import google_checkout

def get_checkout_url(request):
	return google_checkout.get_checkout_url(request)