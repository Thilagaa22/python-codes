import math
def div(n):
  if n % 2 == 0:
    return div(n/2)
  else:
    return math.ceil(n)
n = int(input())
print(div(n))
   
