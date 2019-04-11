def largest(arr,n):
  max = arr[0]
  for i in range(1,n):
    if arr[i]>max:
      max =arr[i]
  return max
 arr = int(input("Enter the number:"))
 n = len (arr)
 ans = largest(arr.n)
 print("largest number",ans)
 
