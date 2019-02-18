'''
 
Write a program that asks the user to enter two numbers a and b. Then, the program calculates the sum of all odd numbers between a and b (inclusive). You need to call the input function twice the get a and b. You need to write this program using a while loop. 

2. Write a program that asks the user to enter two numbers a and b, and prints all positive numbers that are divisible by a and are less than b. For example, if b is 100 and a is 10, print 10 20 30 40 50 60 70 80 90. 

3. Write a program that asks the user for 5 numbers (one at a time) and prints the square root of the number. 

'''

print(">>>Program 1!","Total of all odd numbers added between a and b")
a = int(input('input a: '))
b = int(input('input b: '))
x = a
total = 0
while	a <= b:
	calc = a / 2
	if not((calc).is_integer()):
		total = total + a
		#print(total)
	a = a + 1
print ("Total of all odd numbers added between",x," and ",b," =",total)
print(" "*200)
print(">>>Program 2!","enter numbers for a and b, all positive numbers that are divisible by a and are less than b")
a = int(input('input a: '))
b = int(input('input b: '))
'''a=10
print("a=",a)
b=100
print("b=",b)'''
x = a
total = 0
print("looking for numbers between",x, "and", b ," divisibe by",x)	
while	a <= b:
	calc = a / x
	#print("my math=",b,"/",a)
		#print(calc)
	#print("i am testing",a)
	#print("a=",a,"b=",b)
	if (calc).is_integer():
		total = total + 1
		#print("divisable by", a,"True")
		print(a)
	a = a + 1
print ("number of items divisible by", x, "=" ,total)
print(" "*200)
print('>>>Program 3!',"Enter 5 numbers to squareroot")
x=1
while x <= 5:
	number = int(input('Enter number: '))
#	f = number
	#print(f)
	x = x+1
	from math import sqrt
	c = sqrt(float(number))
	print(c)
print("done.")
	#if x <= 5:
	#	z = number + f
		#print(z)
	#else:
		#c = sqrt(float(z))
		#print(c) 
		
