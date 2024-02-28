#!/usr/bin/env python
# coding: utf8

#Fornecidos três valores, a, b e c, implemente uma função que retorne 
#quantos desses três são iguais. A reposta deve ser 2, se todos são 
#iguais; 1, se dois são iguais ou 0, se todos são distintos entre si. 

def quantos_iguais(a, b, c):
	if (a == b and b == c):
		return 3
	elif ((a == b and b != c and a != c) or (a == c and b != c and a != b) or (b == c and a != c and a != b)):
		return 2
	return 1
	
def main():
	a = input("Informe um número:")
	b = input("Informe um número:")
	c = input("Informe um número:")
	print(str(int(quantos_iguais(a, b, c))) + " iguais.")
	
main()	
