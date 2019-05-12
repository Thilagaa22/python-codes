s = int(input())
p = 1
k = 0
while(s):
  k = s % 10
  p = p * k
  s = s // 10
print(p)
