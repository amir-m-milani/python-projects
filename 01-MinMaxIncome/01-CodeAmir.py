a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
c = int(input("Enter the Number: "))
if a > b and a > c:
    print('Max Value: ', a)
    print(f"Min Value:{b}" if c > b else f"Min Value: {c}")
elif c > b and c > a:
    print('Max Value: ', c)
    print(f"Min Value:{b}" if a > b else f"Min Value: {a}")
else:
    print('Max Value: ', b)
    print(f"Min Value:{a}" if c > a else f"Min Value: {c}")
