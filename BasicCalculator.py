def add (num1,num2):
    return num1+num2
def sub (num1,num2):
    return num1-num2
def mul (num1,num2):
    return num1*num2
print("This is a Basic Calculator Program")
while True:
    var =int (input("press 1 for add, 2 for sub , 3 for mul, 5 for quit:"))
    if var == 1:
        num1= int(input("Enter the num1:"))
        num2= int(input("Enter the num2:"))
        print("sum=",add(num1,num2))
    elif var==2:
        num1= int(input("Enter the num1:"))
        num2=int(input("Enter the num2:"))
        print("sub=",sub(num1,num2))
    elif var ==3:
        num1=int (input("nter the num1:"))
        num2=int(input("nter the num2:"))
        print("mul=",mul(num1,num2))
    elif var==5:
        print("Thanks for using this app")
        break



