#!/usr/bin/env python
# coding: utf8


#2) Faça uma função que determine o quádruplo de um número, usando a função do item anterior. 

def dobro(valor):
	return int(valor) * 2

def quadruplo(numero):
		return dobro(numero) * dobro(numero)

def main():
	numero = input('Qual o valor?')
	resultado = quadruplo(numero)
	print(resultado)

main()
