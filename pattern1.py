a = int(input('Enter the number of rows'))

x = 0
for row in range(1,a+1):
    for num in range(0,row):
        #x = x + 1
        print('+',end= ' ')
    print('\r')
print('\r')


x = 0
for row in range(1,a+1):
    for num in range(0,row):
        x = x + 1
        print(x,end= ' ')
    print('\r')