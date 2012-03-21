from django.shortcuts import render_to_response
from django.template import RequestContext
from djecomstore.cart import cart

def show_cart(request, template_name="cart/cart.html"):
	cart_items = cart.get_cart_items(request)
	cart_item_count = cart_items.count()
	page_title = 'Shopping Cart'
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))