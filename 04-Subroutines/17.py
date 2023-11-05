def different(n1,n2,n3):
    if n1 != n2 != n3:
        return True 
    else:
        return False

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

if different(number1,number2,number3):
    print(f'Numbers {number1}, {number2}, and {number3} are different')

