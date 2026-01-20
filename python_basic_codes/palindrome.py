num=int(input("Enter a number: "))
temp=num  #121
rev=0 #121
while num>0:
  rem=num%10   #1
  rev=rev*10+rem
  num=num//10
print("Reverse: ",rev)
if temp==rev:
  print(f"{rev} is palindrome number")
else:
  print(f"{rev} is not a palindrome number")

  """
  def check_palindrome():
  num=int(input("enter the number"))
  s=str(num)
  if num==int(s[::-1]):
    print("palindrome")
  else:
    print("non palindrome")
check_palindrome()
check_palindrome()
check_palindrome()
check_palindrome()
"""