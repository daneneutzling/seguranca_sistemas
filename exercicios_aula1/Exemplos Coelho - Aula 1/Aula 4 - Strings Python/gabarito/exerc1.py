#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário
#digitar o seu nome e em seguida mostre o nome do usuário de trás para frente 
#utilizando somente letras maiúsculas. 
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

import string
	
def invertido(nome):
	for i in range(len(nome) - 1, -1, -1):
		print(nome[i].upper(), end='')
	
def main():
	palavra = str(input("Qual a palavra?"))
	invertido(palavra)

main()
