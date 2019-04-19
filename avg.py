n = int(input("Enter number to calculate to sum:"))
avg = 0
sum = 0
for num in range(0,n+1,1):
  sum = sum + num
print("sum of first ",n ,"numbers is:",sum)
print(sum/n)
