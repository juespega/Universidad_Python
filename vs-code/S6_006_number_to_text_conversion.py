number = int(input("Enter a number between 1 and 3: "))

if number == 1:
    textnumber = 'Number one'
elif number == 2:
    textnumber = 'Number two'
elif number == 3:
    textnumber = 'Number three'
else:
    textnumber = 'value out of range'

print(f'number provided {number} : {textnumber}')