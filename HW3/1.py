def SumofOddNumbers(a,b):
  total = 0
  while b%2 == 0:
    num = input ("Please enter 2 numbers: ")
    for x in range(a,b):
      if x % 2 == 0:
        total = total + x
    return total + b
  else:
    for x in range(a,b):
      if x % 2 != 0:
        total = total + x
    return total + b
    
# can't figure out how to let user input - I figured how to solve the addition of all odds within the range, but can't get input
