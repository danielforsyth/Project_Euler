def fib(a,b):
	print a
	print b
	num = 0
	count = 0
	if b %2 ==0:
		count += b
	while num <4000000:
		num = a + b
		print num
		if num %2 == 0:
			count +=num
		a = b
		b = num

	print "Toal = ", count


fib(1,2)
