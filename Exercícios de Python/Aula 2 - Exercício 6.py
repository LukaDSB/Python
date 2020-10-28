salb = float(input('Insira o Salário Bruto: '))
valorp = int(input('Insira valor da prestação: '))
regra = salb*0.3

if valorp <= regra:
    print ('Crédito concedido')

else:
    print ('Crédito Negado')
    
