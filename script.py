lower = int(input("Enter a lower limit:"))
upper = int(input("Enter a upper limit:"))
print("even numbers between",lower ,"and", upper ,"are:")
for num in range(lower,upper):
  if num >1:
    for i in range(2,num):
      if(num % 2) != 0:
        break
    else:
      print(num)
