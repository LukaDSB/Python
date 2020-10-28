
print ('Selecione um prato: ')
print ('1 - Vegetariano')
print ('2 - Peixe')
print ('3 - Frango')
print ('4 - Carne')
prato = int(input())

print('Selecione uma sobremesa:')
print('1 - Abacaxi')
print('2 - Sorvete')
print ('3 - Mousse Diet')
print ('4 - Mousse Chocolate')
sobremesa = int(input())

print ('Selecione uma bebida:')
print ('1 - Chá')
print ('2 - Suco de Laranja')
print ('3 - Suco de Melão')
print ('4 - Refrigerante Diet')
bebida = int(input())

if prato == 1:
    prato = 180
    P = ('Vegetariano')

if prato == 2:
    prato = 230
    P = ('Peixe')

if prato == 3:
    prato = 250
    P = ('Frango')

if prato == 4:
    prato = 350
    P = ('Carne')
    
if sobremesa == 1:
    sobremesa = 75
    S=('Abacaxi')

if sobremesa == 2:
    sobremesa = 110
    S=('Sorvete Diet')
    
if sobremesa == 3:
    sobremesa = 170
    S=('Mousse Diet')
    
if sobremesa == 4:
    sobremsa = 200
    S=('Mousse Chocolate')

if bebida == 1:
    bebida = 20
    B=('Chá')

if bebida == 2:
    bebida = 70
    B=('Suco de Laranja')

if bebida == 3:
    bebida = 100
    B = ('Suco de Melão')

if bebida == 4:
    bebida = 65
    B = ('Refrigerante Diet')

caloriatotal = (prato + sobremesa)

print ('----- Seu Pedido ----')
print (' Prato: ',P,'\n', 'Sobremesa: ',S,'\n','Bebida: ',B,'\n')
print('Calorias do seu prato: ', caloriatotal)
