'''
	Manipulação de listas com o python usando função
'''
def listaTodos(t):
	print('-------------------------------')	
	for i in range(t): # percorre todo o vetor
		print(aluno[i], nota[i], end = ' ')
		if nota[i] >= 6:
			print('Aprovado')
		else:
			print('Reprovado')
	print('-------------------------------')
		
def aprovados(t):
	print('Lista de Aprovados')
	for i in range(t):
		if nota[i] >= 6:
			print(aluno[i], nota[i], 'Aprovado')
			
def reprovados(t):
	print('Lista de reprovados')
	for i in range(t):
		print(aluno[i], nota[i], end = ' ')
		if nota[i] < 6:
			print('Reprovado')
			
aluno = ['Maria','Juca','Julia','Ana','Rita','Ruy','Tico','Carla']
nota = [10,4,7,3,6, 7, 8, 4]
opcao = 1
while opcao != 0:
	tamanho = len(aluno) # quantidade de elementos
	print('')
	print('---------------')
	print('Escolha a opção')
	print('---------------')
	print('1 - lista todos')
	print('2 - lista Aprovados')
	print('3 - lista Reprovados')
	print('4 - Inserir novo aluno e nota')
	print('0 - Sai do programa')
	opcao = int(input('Opção ==>> '))
	if opcao == 1:
		listaTodos(tamanho)
	elif opcao == 2:
		aprovados(tamanho)
	elif opcao == 3:
		reprovados(tamanho)	
	elif opcao == 4:
		print('-----------------')
		print('Cadastro de aluno')
		print('-----------------')
		a = input('Nome do aluno: ')
		n = int(input('Nota do aluno'))
		aluno.append(a)
		nota.append(n)
		