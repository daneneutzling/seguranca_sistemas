#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

#2) Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical em maiuscula.
#F
#U
#L
#A
#N
#O

def main():
	nome = input("Qual o nome?")
	for i in range(0, len(nome)):
		print(nome[i:(i + 1)].upper())

main()	
