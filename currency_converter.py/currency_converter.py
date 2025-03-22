exchange_rate = {
	'EUR': {'USD': 1.1, 'GBP': 0.85},
	'USD': {'EUR': 0.91, 'GBP': 0.77},
    'GBP': {'EUR': 1.18, 'USD': 1.3}
}


def currency_converter(amount, from_currency, to_currency):
	try:
		amount = float(amount)
	except:
		return 'InvalidValue'
	if from_currency not in exchange_rate or to_currency not in exchange_rate[from_currency]:
		return 'Currency not registered.'

	rate = exchange_rate[from_currency][to_currency]

	converted_amount = amount * rate

	return f'{amount} in {from_currency} is {converted_amount} in {to_currency}.'

print(currency_converter(100,'EUR', 'GBP'))
print(currency_converter(100, 'GBP', 'USD'))
print(currency_converter('ffe', 'EUR', 'USD'))
print(currency_converter(100, 'efd', 'EUR'))