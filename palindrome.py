def palindrome(str):
  rev = ''.join(reversed(str))
  if( str == rev):
    return Ture
  return False
n= input("Enter a string")
ans = palindrome(n)
if (ans):
  print("This string is palindrome")
else:
  print("This string is not palindrome")
