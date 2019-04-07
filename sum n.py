n = int(input("Enter the sum of number:"))
if n>0: 
  print("positive numbers only accepted")
sum = 0
for num in range(n+1):
  sum = sum + num
print("Sum of first ",n,"numbers is:",sum)
