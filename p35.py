class Rectangle:
    def __init__(self,leng,wid):
        self.leng=leng
        self.wid=wid

    def cal_area(self):
        return self.leng * self.wid

leng=float(input("Enter a length:"))
wid=float(input("Enter a width:"))

rectangle = Rectangle(leng,wid)

area = rectangle.cal_area()
print("The area of the rectangle is:",area)
