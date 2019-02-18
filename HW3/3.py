counter = 0
while True and counter < 6:
    num = input("Enter a number: ")
    if num == 'x':
	break
    else:
	number = float(num)
	number_sqrt = number ** (0.5)
	print("Square Root of %0.2f is %0.2f" %(number, number_sqrt))
	counter += 1
    