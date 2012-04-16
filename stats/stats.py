import os
import base64

def tracking_id(request):
	try:
		return request.session['tracking_id']
	except KeyError:
		request.session['tracking_id'] = base64.b64encode(os.urandom(36))
		return request.session['tracking_id']