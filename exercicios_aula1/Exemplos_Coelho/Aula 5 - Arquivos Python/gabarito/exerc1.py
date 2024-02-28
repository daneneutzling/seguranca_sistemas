#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = 'Rafael Vieira Coelho'
__DATE__ = '4/4/2019'

# 2) Faça um programa para gerenciar uma agenda de contatos. 
# Para cada contato armazene o nome, o telefone e o aniversário. 
# O programa deve permitir 

# (1) inserir contato, 
# (2) remover contato, 
# (3) pesquisar um contato pelo nome, 
# (4) listar todos os contatos, 
# (5) listar os contatos cujo nome inicia com uma dada letra, 
# (6) salvar dados em arquivo. 

# Sempre que o programa for encerrado, os contatos devem ser armazenados em um arquivo. 
# Quando o programa iniciar, os contatos devem ser lidos do mesmo arquivo.


import json


def cadastra(pessoas):
	nome = input("Informe o nome: ")
	fone = input("Informe o telefone: ")
	aniversario = input("Informe a data de aniversário: ")
	pessoas.append({"nome":nome,"fone":fone,"aniversario":aniversario})

def salva(pessoas):
	try:
		arquivo = open('agenda.txt', 'w')  
		for pessoa in pessoas:
			arquivo.write(pessoa["nome"] + '\t' + pessoa["fone"] + '\t' + pessoa["aniversario"] + '\n')
		arquivo.close()
		print("Dados salvos com sucesso.")
	except:
		print("Erro ao salvar dados!")
		
def carrega_dados():
	pessoas = []
	try:
		arquivo = open('agenda.txt', 'r') 
		for linha in arquivo:
			dados = linha.split('\t')
			pessoas.append({"nome":dados[0],"fone":dados[1],"aniversario":dados[2].split('\n')[0]})
		arquivo.close()
	except:
		print("Erro ao ler dados da agenda.")	
	return pessoas
	
def mostra_todos(pessoas):
	for p in pessoas:
		print('Nome: ' + p['nome'])
		print('Telefone: ' + p['fone'])
		print('Aniversário: ' + p['aniversario'] + '\n')

def mostra(pessoas, letra_inicial):
	for p in pessoas:
		if (p['nome'].startswith(letra_inicial)): 
			print('Nome: ' + p['nome'])
			print('Telefone: ' + p['fone'])
			print('Aniversário: ' + p['aniversario'] + '\n')

def pesquisa(pessoas, nome):
	for p in pessoas:
		if (nome in p['nome']): 
			print('Nome: ' + p['nome'])
			print('Telefone: ' + p['fone'])
			print('Aniversário: ' + p['aniversario'] + '\n')

def remover(pessoas, nome):
	achou = False
	for p in pessoas:
		if (nome in p['nome']): 
			pessoas.remove(p)
			print(nome + " removido com sucesso")
			achou = True
			break;
	if (not achou):
		print(nome + " não encontrada na agenda.")
			
def menu():
	print ("\n" * 100)
	print("MENU:")
	print("(1) inserir contato")
	print("(2) remover contato")
	print("(3) pesquisar um contato pelo nome")
	print("(4) listar todos os contatos")
	print("(5) listar os contatos cujo nome inicia com uma dada letra")
	print("(6) salvar dados em arquivo")
	print("(7) sair")
	return int(input("Qual a sua opção? "))

def main():
	pessoas = carrega_dados()
	opcao = menu()
	while (opcao != 7):
		if (opcao == 1):
			cadastra(pessoas)
		elif (opcao == 2):
			nome = input("Qual a nome a ser removido? ")
			remover(pessoas, nome)
		elif (opcao == 3):
			nome = input("Qual a nome a ser pesquisado? ")
			pesquisa(pessoas, nome)		
		elif (opcao == 4):
			mostra_todos(pessoas)
		elif (opcao == 5):
			letra_inicial = input("Qual a letra inicial? ")
			mostra(pessoas, letra_inicial)		
		elif (opcao == 6):
			salva(pessoas)
		input("Pressione ENTER para voltar ao menu")	
		opcao = menu()	

main()
