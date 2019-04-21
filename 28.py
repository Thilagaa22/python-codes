def re(arr,n):
  temp = [0] * n
  for i in range(0,n):
    temp[arr[i]] = i
  for i in range(0,n):
    arr[i]=temp[i]
  def pri(arr,n):
    for i in range(0,n):
      print(arr[i],end="")
      arr = [1,4,0,7]
      n = len(arr)
      print(pri(arr,n))
      re(arr,n)
      print(pri(arr,n))
