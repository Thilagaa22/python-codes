x = int(input("Enter limits of numbers:"))
n1 = 0
n2 = 1
count = 0
elif x == 1:
  print("Fibonacci sequance upto",x,":")
  print(n1)
else:
  print("Fibonacci sequance upto",x,":")
  while count < x:
    print(n1,end=',')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    
