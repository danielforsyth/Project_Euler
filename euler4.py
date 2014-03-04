def three_product():
	pals = []
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			product = i*j
			string = str(product)
			if string[::-1] == string:
				pals.append(product)
	print max(pals)

three_product()
			



