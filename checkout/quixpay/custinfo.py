from quix.pay.transaction import CreditCard, Address, Customer
from quix.pay.gateway.authorizenet import AimGateway
import quixpay

card = CreditCard(
	number = '4111111111111111',
	month = '10',
	year = '2020',
	first_name = 'John',
	last_name = 'Doe',
	code = '123'
)

address = Address(
	first_name = 'Test',
	last_name = 'Bob',
	address1 = '1234 Fake St.',
	company = 'Test Company',
	city = 'Fakeville',
	state_province = 'TX',
	country = 'US',
	postal_code = '12345',
	phone = '(555) 555-5555'
)

customer = Customer(
	cust_id = '1234',
	email = 'customer@fakeperson.com',
	ip = '255.255.255.255',
	billing_address = address,
	shipping_address = address
)

gateway = AimGateway('6mZxu88KF89', '4J89zqLr5Te9t9JN')
gateway.use_test_mode = True
gateway.use_test_url = True

response = gateway.sale(1.00, card, customer=customer)

if response.status == response.APPROVED:
	for key, value in response.gateway_data.iteritems():
		print "%s = %s" % (key, value)
else:
	sys.exit("%s %s" % (response.status_strings[response.status], response.message))
	
print "Transaction %s = %s (%d): %s" % (response.trans_id, 
								    response.status_strings[response.status],
								    response.status,
								    response.message)