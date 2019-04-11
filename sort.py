def sort(array,n):  
  for i in range(n):
  array[i] = i + 1
if __name__ == "__main__":
  arr=int(input("Enter a number"))
  n = len (arr)
  sort(arr,n)
  for i in range(n):
    print(arr[i],end="")
