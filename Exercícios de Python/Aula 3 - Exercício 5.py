nome = list(range(3))
idade = list(range(3))
sexo = list(range(3))

for i in range (3):
    nome[i] = input('Insira o Nome: \n')
    idade[i] = int(input('Insira a idade: \n'))
    sexo[i] = input('Sexo: (Digite 1 para Masculino e 2 para Feminino\n')

for i in range (3):
    if idade[i] >= 21:
        if sexo[i] == 1:
            print ('Nome: ', nome[i])
