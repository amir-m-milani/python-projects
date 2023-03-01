a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
c = int(input("Enter the Number: "))
if a > b and a > c:
    print('Max Value: ', a)
elif c > b and c > a:
    print('Max Value: ', c)
else:
    print('Max Value: ', b)
