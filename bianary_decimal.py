def return_deca(binary):
	binary = binary[::-1]
	binary_holder = 1
	deca_result = int()
	for i in binary:
		if int(i) == 1:
			deca_result += binary_holder
		binary_holder *= 2
	return deca_result
def return_binary(deca):
	def return_down_place_list(number):
		_list = list()
		num = 1
		while True:
			if num > number:
				return _list
				break
			_list.append(num)
			num **= 2
	print(return_down_place_list(15))
return_binary(12)
