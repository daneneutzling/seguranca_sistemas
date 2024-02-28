#!/usr/bin/env python
# coding: utf8

# Escreva uma função chamada mais_frequentes que receba uma string 
# e escreva na tela as letras em ordem decrescente de ocorrência. 

import string

def mais_frequentes(texto):
	letras = string.ascii_lowercase
	i = 0
	conta_letras = [0] * 26
	texto = texto.replace(" ", "").lower()
	for i in range(0, len(letras)):
		conta_letras[i] = texto.count(letras[i])
	
	total = 0
	for i in range(0, len(letras)):
		if (conta_letras[i] != 0):
			print("%c - %d - %.2f%%" % (letras[i], conta_letras[i], int(conta_letras[i] / len(texto) * 100)))
			total += conta_letras[i]
	print("\nTotal: %d letras (100%%)" % total)
	
def main():
	texto = input("Informe o texto: \n")
	mais_frequentes(texto)

main()	
