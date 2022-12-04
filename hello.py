def fun1():
    a=int(input("Enter your Number"))
    b=int(input("Enter your number"))
    c=a+b
    print("The Sum is :",c)
def fun2():
    a=int(input("Enter your Number"))
    b=int(input("Enter your number"))
    c=a-b
    print("The Difference is :",c)
def fun3():
    a=int(input("Enter your Number"))
    b=int(input("Enter your number"))
    c=a*b
    print("The Product is :",c)
def fun4():
    a=int(input("Enter your Number"))
    b=int(input("Enter your number"))
    c=a/b
    print("The Divident is :",c)
while True:
    print("Addittion:"
          "Subtraction:"
          "Multiplication"
          "Division")
    ch=int(input("enter your choice:"))
    if ch==1:
        fun1()
    elif ch==2:
        fun2()
    elif ch==3:
        fun3()
    elif ch==4:
        fun4()
    else:
        print("Invalid input")
        break
           
           

