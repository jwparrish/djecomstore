from quix.pay.gateway.authorizenet import AimGateway
from quix.pay.transaction import CreditCard

card = CreditCard(
	number = '4111111111111111',
	month = '10',
	year = '2020',
	first_name = 'John',
	last_name = 'Doe',
	code = '123'
)



#response = gateway.sale(1.00, card)

#print "Transaction %s = %s (%d): %s" % (response.trans_id, 
#								    response.status_strings[response.status],
#								    response.status,
#								    response.message)