'''
Crie um dicionário que é uma agenda e coloque nele os seguintes dados: 
chave (cpf),nome, idade, telefone (podem ser uma tupla ou lista). 

O programa deve ler um número indeterminado de dados, criar a agenda 
e imprimir todos os itens do dicionário no formato: nome-idade-fone.
'''

#!/usr/bin/env python
# coding: utf8

def main():
	agenda = {}
	while True:
		op = input('Quer continuar [S/N]?').upper() 
		if op == 'N':
			break
		cpf = int(input('Qual o cpf?'))
		nome = input('Qual o nome?')
		idade = int(input('Qual o idade?'))
		telefone = input('Qual o telefone?')
		agenda[cpf] = (nome, idade, telefone)
	
	for cpf in sorted(agenda.keys()):
		print(agenda[cpf][0],'-',agenda[cpf][1],'-',agenda[cpf][2])	
		
main()
