#!/usr/bin/env python
# coding: utf8

# 1) Crie um programa que receba como entrada do usuário o número de alunos de uma disciplina. 
# Devem ser lidos os nomes e as notas dos três trimestres e do exame caso haja necessidade. 
# Salve em um arquivo texto chamado media.txt o nome, se passou e a média final de todos os alunos lidos 
# (use o \t para separar o nome da média ao escrever no arquivo).

def leitura(texto):
	try:
		nota = float(input(texto))
	except:
		nota = 0
	return nota	


def calcula_media(nota1, nota2, nota3, arquivo):
	media = (nota1 + nota2 + nota3) / 3
	if (media < 7):
		exame = leitura("Exame: ")
		media = (nota1 + nota2 + nota3 + exame) / 4
		if (media >= 5):
			arquivo.write("Aprovado (em exame) \t")
		else:
			arquivo.write("Reprovado. \t")	
	else:
		arquivo.write("Aprovado \t")
	return media		

def salva_alunos(nome_arquivo):
	numero_alunos = int(input("Quantos alunos?"))
	f = open(nome_arquivo, "w")

	for i in range(numero_alunos):
		nome = input("Nome: ")
		f.write(nome + "\t")
		nota1 = leitura("Nota 1: ")	 	
		nota2 = leitura("Nota 2: ")	 	
		nota3 = leitura("Nota 3: ")	 	
		media = calcula_media(nota1, nota2, nota3, f)
		f.write("%.1f \n" % media)
	f.close() 

def mostrar_alunos_salvos(nome_arquivo):
	f = open(nome_arquivo, "r")
	for linha in f:
		aluno = linha.split("\t")
		print("Nome: %s \t  Status: %s \t Média Final: %s" % (aluno[0], aluno[1], aluno[2]))
	f.close()	

def main():
	salva_alunos("alunos.txt")
	mostrar_alunos_salvos("alunos.txt")
	
main()	
