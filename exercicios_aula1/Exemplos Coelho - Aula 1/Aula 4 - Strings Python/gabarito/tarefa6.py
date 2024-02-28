#!/usr/bin/env python
# coding: utf8

__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

#Crie a função ehMaiusculo(ch) e ehNumero(ch)

import string

def ehMinusculo(letra):
	return string.ascii_lowercase.find(letra) != -1
	
def ehMinusculo2(ch):
	return ch in string.ascii_lowercase
	
def ehMinusculo3(ch):
	return 'a' <= ch <= 'z'		
	
def ehMaiusculo(letra):
	return string.ascii_uppercase.find(letra) != -1
	
def ehNumero(letra):
	return string.digits.find(letra) != -1	
	
def main():
	letra = input("Qual o caractere?")
	if (ehMinusculo3(letra)):
		print("É minúsculo")
	else:
		print("Não é minúsculo")	
		
	if (ehMaiusculo(letra)):
		print("É maiúsculo")
	else:
		print("Não é maiúsculo")	

	if (ehNumero(letra)):
		print("É número")
	else:
		print("Não é número")	

main()	
