num = int (input("please ennter any number:"))
count = 0 
while(num > 0):
  num = num//10
  count = count + 1
print("\n Number of digits in a given number: %d" %count)
