num=int(input("Enter number: ")) #1001->4
digit=0
rev=0

while num!=0:
  rem=num%10
  rev=rev*10+rem
  digit=digit+1
  num=num//10

print("Number of digits:",digit)