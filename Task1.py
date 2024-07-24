#simple calculator
def add(x,y):
    print(f"sum of {x}+{y}=",x+y)

def sub(x,y):
    print(f"sub of {x}-{y}=",x-y)

def mul(x,y):
    print(f"product of {x}x{y}=",x*y)

def div(x,y):
    print(f"div of {x}/{y}=",x/y)

def user():
    while True:
        print('''select an option
    ----------------
    1. Add
    2. Sub
    3. Multiplication
    4. Division
    5. quit

    ''')
        query = int(input("enter an option : "))
        if query == 5:
            print("Thanks ")
            break
        elif query > 5:
            print("Please enter valid option")
        else:            
            x=int(input("enter the 1st no: "))
            y=int(input("enter the 2nd no: "))
            if query==1:
                add(x,y)
            elif query==2:
                sub(x,y)
            elif query==3:
                mul(x,y)
            elif query==4:
                div(x,y)
            else:
                print("!!!enter valid option!!!")
user()
