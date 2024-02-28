#!/usr/bin/env python
# coding: utf8

'''
Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) 
e depois coloque em um dicionário. Depois remova todas as pessoas menores 
de 18 anos do dicionário e coloque em outro dicionário. Use o cpf como chave.
'''
def leitura_contatos():
	agenda = {}
	while (True):
		print("Informe o CPF zero quando quiser parar de informar contatos.")
		cpf = int(input("CPF: "))
		if (cpf == 0):
			break
		nome = input("Nome: ")
		idade = int(input("Idade: "))
		agenda[cpf] = (nome, idade)	
	return agenda	

def main():
	agenda = leitura_contatos()
	
	agenda_para_maiores = {}
	for cpf in agenda.keys():
		contato = agenda.get(cpf)
		if (int(contato[1]) >= 18):
			agenda_para_maiores[cpf] = agenda.get(cpf) 
	print(agenda_para_maiores)		
	
main()	
