firstPersonName = input('Enter first person name: ')
firstPersonAge = int( input('Enter first person age: ') )
secondPersonName = input('Enter second person name: ')
secondPersonAge = int( input('Enter second person age: ') )

if firstPersonAge >= 18 and secondPersonAge >= 18:
    print(f'Both {firstPersonName} and {secondPersonName} are adults')
elif firstPersonAge >= 18 and secondPersonAge < 18:
    print(f'Only {firstPersonName} is adult')
else:
    print(f'Only {secondPersonName} is adult')