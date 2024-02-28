#!/usr/bin/env python
# coding: utf8

#1) Faça uma função que determine o dobro de um número. 

def dobro(valor):
	return int(valor) * 2
	
def main():
	numero = input('Qual o valor?')
	resultado = dobro(numero)
	print(resultado)

main()		
