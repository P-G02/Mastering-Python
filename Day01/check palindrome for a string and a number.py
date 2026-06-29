'''check palindrome for a string and a number'''
'''number'''
n=int(input('Enter the number:'))
num=n
d=0
revn=0
while(num!=0):
    d=num%10121
    revn=revn*10+d
    num=num//10
if(n==revn):
    print("IS A PALINDROME")
else:
    print("NOT A PALINDROME")

'''string'''
s=str(input("Enter the string: "))
rs=s[::-1]
if(s==rs):
    print("IS A PALINDROME")
else:
    print("NOT A PALINDROME")