def main():
	dicionario = {'Joao':(10, 'Turma B'), 'Maria':(9, 'Turma A')}
	print('original:', dicionario)
	dicionario = dict(sorted(dicionario.items(), reverse=True))
	print('decrescente pelo nome(chave):', dicionario)
	dicionario = dict(sorted(dicionario.items(), reverse=False))
	print('crescente pelo nome(chave):', dicionario)
	dicionario = dict(sorted(dicionario.items(), key=lambda item: item[0], reverse=True))
	print('decrescente pela nota:', dicionario)
	dicionario = {'Joao':(10, 'Turma B'), 'Maria':(9, 'Turma A')}
	dicionario = dict(sorted(dicionario.items(), key=lambda item: item[0], reverse=False))
	print('crescente pela nota:', dicionario)
	dicionario = {'Joao':(10, 'Turma B'), 'Maria':(9, 'Turma A')}
	dicionario = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
	print('decrescente pela turma:', dicionario)
	dicionario = {'Joao':(10, 'Turma B'), 'Maria':(9, 'Turma A')}
	dicionario = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=False))
	print('crescente pela turma:', dicionario)

if __name__ == '__main__':
	main()
