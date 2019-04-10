lower = int(input("Enter a lower limit:"))
upper = int(input("Enter a upper limit:"))
print("prime numbers are between", lower, "and",upper, "are:")
for num in range(lower,upper +1):
  if num > 1:
    for i in range(2,num):
      if( num % i )==0:
        break
    else:
      print(num)
   
