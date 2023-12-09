"""
El usuario debe proporcionar la siguiente informacion:
- Nombre del libro
- ID del libro (númerico)
- Precio del libro (flotante)
- Indicar si el envio es gratuito (Verdadero / Falso)

Desplegar esta misma información:
"""

print('Please provide the following information:')
print()
name = input('Name of the book: ')
id = int(input('Id of the book: '))
price = float(input('Price of the book: '))
shipment = input('Free shipping (True / False): ')

if shipment == 'True':
    shipment = True
elif shipment == 'False':
    shipment = False
else:
    print('Wrong value must write True or False')

print(f'''
    Name: {name}
    ID: {id}
    Price: {price}
    Free shipping: {shipment}
''')