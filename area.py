def arearec(x,y):
    return x*y

def periRec(x,y):
    return x+x+y+y

def areaSquare(x):
    return x*x

if __name__=="__main__":
    n1=int(input("Enter value1"))
    n2=int(input("Enter value2"))
    print(arearec(n1,n2))
    print(periRec(n1,n2))
    print(areaSquare(n1))

while(True):
    print('''
          1. Area of rectangle
          2. Perimeter of Rectangle
          3. Area of Square
          ''')
    ch = int(input("enter your choice"))
    if ch == 1:
        print(arearec(n1, n2))
    elif ch == 2:
        print(periRec(n1, n2))
    elif ch == 3:
        print(areaSquare(n1))
    else:
        print("Invalid choice")