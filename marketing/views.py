from django.http import HttpResponse
from djecomstore.settings import CURRENT_PATH
import os

ROBOTS_PATH = os.path.join(CURRENT_PATH, 'marketing/robots.txt')

def robots(request):
	return HttpResponse(open(ROBOTS_PATH).read(), 'text/plain')
	