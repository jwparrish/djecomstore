from django.test  import TestCase, Client
from django.core import urlresolvers
from django.contrib.auth import SESSION_KEY

import httplib

class NewUserTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		logged_in = self.client.session.has_key(SESSION_KEY)
		self.assertFalse(logged_in)
	
	def test_view_homepage(self):
		home_url = urlresolvers.reverse('catalog_home')
		response = self.client.get(home_url)
		# check that we did get a response
		self.failUnless(response)
		# check that status code of response was success
		# (httplib.OK = 200)
		self.assertEqual(response.status_code, httplib.OK)
