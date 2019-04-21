num = [1,2,3,4,5]
n = len(num)
num.sort()
if n %2==0:
  m1 = num[n//2]
  m2 = num[n//2-1]
  m = (m1+m2)/2
else:
  m = num[n//2]
  print(m)
  
