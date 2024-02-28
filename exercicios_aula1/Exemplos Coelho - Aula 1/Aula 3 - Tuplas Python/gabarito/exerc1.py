'''
1) Considere um sistema onde os dados são armazenados em dicionários. 
Nesse sistema existe um dicionário principal e o dicionário de backup. 
Cada vez que o dicionário principal atinge tamanho 5, 
ele imprime os dados na tela e apaga o seu conteúdo. 

Crie um programa que insira dados em um dicionário, realizando o backup 
a cada dado e excluindo os dados do dicionário principal quando ele atingir tamanho 5.
'''

#!/usr/bin/env python
# coding: utf8

def main():
	principal = {}
	backup = {}
	contador = 0
	while True:
		op = input('Quer continuar [S/N]?').upper() 
		if op == 'N':
			break
		nome = input('Qual o nome?')
		idade = int(input('Qual a sua idade?'))
		contador += 1
		principal[nome] = idade	
		if contador == 5:
			backup = principal
			principal = {}
			print(backup)
			contador = 0
main()
