n = int(input())
s = 0
while(n):
  k = n % 10
  s = s * 10 + k
  n = n // 10
print(s)
