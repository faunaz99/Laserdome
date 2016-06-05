##!/usr/bin/env python3

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def run(run):
    return main() 

def main():
    operation = input("what do you want to do? (+,-,*,/): ")
    if(operation != '+'
       and operation != '-'
       and operation != '*'
       and operation != '/'):

        #inavild operation
        print("invalid operation")
    else:
        var1 = int(input("enter num1: "))
        var2 = int(input("enter num2: "))
        if(operation == '+'):
            print(add(var1, var2))
        elif(operation == '-'):
            print(sub(var1, var2))
        elif(operation == '*'):
            print(mul(var1, var2))
        else:
            print(div(var1, var2))

    loop = input("want to try again (yes/no): ")
    if(loop == "yes"):
        run(main())
    if(loop == "no"):
        quit()
    else:
        loop = input("want to try again (yes/no): ")
        if(loop == "yes"):
            run(main())
        if(loop == "no"):
            quit()
        else:
            quit()

main()
