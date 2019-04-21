import math
def isPerfectSquare(x):
  sr = math.sqrt(x)
  return((sr - math.floor(sr)) == 0 )
x = int()
if (isPerferctSquare(x)):
  print("Yes")
else:
  print("No")
