def power(n):
  if n <= 0:
    return False
  else:
    return n & (n - 1) == 0
n = int(input("Enter a number:"))
if power(n):
  print("{} is a power of two.".format(n))
else:
  print("{} is not a power of two.".format(n))
