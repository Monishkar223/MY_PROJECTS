
import math

def basic_operations():
    print("\n Basic Operations:+,-,*,/")

    num1=float(input("Enter the first number: "))
    op=input("Enter operator: ")
    num2=float(input("Enter the second number: "))

    if op=='+':
        print("Result:",num1+num2)
    elif op=='-':
        print("Result:",num1-num2)
    elif op=='*':
        print("Result:",num1*num2)
    elif op=='/':
        if num2!=0:
            print("Result:",num1/num2)
        else:
            print("Error:Division by zero")
    else:
        print("Invalid operator.")


def advanced_operations():

    print("\nAdvanced operations: sin, cos, tan,sqrt,power")
    op=input("Enter operation: ")
    if op in ['sin','cos','tan','log','sqrt']:
        num=float(input("Enter number: "))

        if op =='sin':
            print("Result:",math.sin(math.radians(num)))

        elif op=='cos':
            print("Result:",math.cos(math.radians(num)))
        elif op=='tan':
            print("Result:",math.tan(math.radians(num)))   
        elif op=='log':
            if num>0:
                print("Result:",math.log(num))
            else:
                print("Error: log undefined for non-positive number.")
        elif op=='sqrt':
            if num>=0:
                print("Result:",math.sqrt(num))
            else:
                print("Error: sqrt undefined for negative numbers.")
    elif op== 'power':
        base=float(input("Enter base: "))
        exponent=float(input("Enter exponent: "))
        print("Result:", math.pow(base, exponent))
    else:
        print("Invalid operation.")
def main():
    print("===Scientific Calculator===")
    while True:
        print("\nSelect mode:")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            advanced_operations()
        elif choice == '3':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice. Try again.")

main()






    
    




        

    
    
