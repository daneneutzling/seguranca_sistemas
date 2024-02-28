#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

#3) Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

#F
#FU
#FUL
#FULA
#FULAN
#FULANO

def main():
	nome = input("Qual o nome?")
	for i in range(0, len(nome)):
		print(nome[0:i].upper())

main()	
