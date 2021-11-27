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
			num *= 2
	num_holder = deca
	final_result = str()
	for i in return_down_place_list(deca)[::-1]:
		if num_holder >= i:
			num_holder -= i
			final_result += "1"
		else:
			final_result += "0"
	return final_result

