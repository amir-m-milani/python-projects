a = int(input())
b = int(input())
c = int(input())

if (a>b):
    if (b>c):
        print("MinIncome:",c,'\n', "MaxIncome:",a)
    else:
        print("MinIncome:",b,'\n', "MaxIncome:",a)

elif (b>a):
    if (a>c):
        print("MinIncome:",c,'\n', "MaxIncome:",b)
    else:
        print("MinIncome:",a,'\n', "MaxIncome:",b)

else:
    if (a>b):
        print("MinIncome:",b,'\n', "MaxIncome:",c)
    else:
        print("MinIncome:",a,'\n', "MaxIncome:",c)
