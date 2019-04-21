n1,n2 = map(int,input().split())
for i in range(n1+1,n2):
  rev = i
  k = 0
  sum =0
  rev = i
  dig = 0
  while(rev):
    rev = rev // 10
    dig = dig + 1
  while(i):
    k = i % 10
    sum = sum + k ** dig
    i = i // 10
  if(rev == sum):
    print(rev)
