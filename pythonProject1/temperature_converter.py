def temperature_converter(number, unit):
	try:
		number = float(number)
	except ValueError:
		return 'Invalid Value!'
	if unit == 'C':
		return f'{number} celsius is {number * (9/5) + 32} fahrenheit.'
	elif unit == 'F':
		return f'{number} fahrenheit in {((number - 32) * 5) / 9} celsius.'
	elif unit != 'C' or 'F':
		return 'Invalid unit!'


print(temperature_converter(25, 'C'))
print(temperature_converter(89.6, 'F'))
print(temperature_converter(89.6, 'b'))

