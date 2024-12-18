class Test:
    def add(self,a,b):
        res=a+b
        return res
    def sub(self,a,b):
        res=a-b
        print("The subtraction of two numbers is:",res)
    def mul(self,a,b):
        res=a*b
        print("The multiplication of two numbers is:",res)
    def div(self,a,b):
        res=a/b
        print("The division of two numbers is:",res)

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))

T=Test()
ans=T.add(a,b)
print("The addition of two numbers is:",ans)

T.sub(a,b)
T.mul(a,b)
T.div(a,b)
