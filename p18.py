num=int(input("Enter a number:"))
temp=num;
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("The reverse is:",rev)

if (temp==rev):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")
