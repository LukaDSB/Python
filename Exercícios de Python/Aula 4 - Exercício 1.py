vetor = list(range(3))

for i in range (3):
    vetor[i] = int(input ('Insira o número: '))
    
busca = int(input ('digite o valor que deseja buscar: '))

for i in range (3):
    if busca == vetor[i]:
        print ('Valor buscado foi encontrado: ', busca)
    else:
        print ('Valor não encontrado')
        
