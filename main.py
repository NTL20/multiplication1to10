valid1 = False
num1 = 0
while not valid1:
    num1 = input('Enter the number you want the multiplication table of:')
    if num1.isdigit() == False:
        print('Invalid Input')
        valid1 = False
    else:
        valid1 = True
else:
    valid1 = True
num1 = int(num1)
print('The Multiplication Table For:', num1)
for count in range(1, 11):
   print(num1, '*', count, '=', num1 * count)
