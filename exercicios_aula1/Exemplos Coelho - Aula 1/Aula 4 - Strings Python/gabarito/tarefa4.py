#!/usr/bin/env python
# coding: utf8


__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

#Escreva uma função que tome uma string como argumento e devolva suas 
#letras de trás para frente, uma por linha.

def invertido(palavra):
	tamanho = 0 - len(palavra) - 1
	for i in range(-1, tamanho, -1):
		print(palavra[i], end = '') # a opção end='' permite não dar ENTER no final de cada print

def main():
	palavra = input("Qual a palavra?")
	invertido(palavra)

main()				
