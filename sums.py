n = int(input("Ener a number:"))
tot = 0
while(n > 0):
  dig = n % 10
  tot = tot + dig
  n = n // 10
print("The total sum of digit is:",tot)
