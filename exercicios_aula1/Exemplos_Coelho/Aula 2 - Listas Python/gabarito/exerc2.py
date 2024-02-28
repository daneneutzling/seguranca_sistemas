#!/usr/bin/env python
# coding: utf8

# 2) Faça um Programa que leia 10 caracteres separadamente (um por vez), e diga quantas consoantes foram lidas. Imprima as consoantes.

import string

def eh_consoante(letra):
	return letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u'

def main():
	letras = []
	lista_consoantes = []
	consoantes = 0
	for i in range(0, 10):
		letras.append(input("Letra " + str(i + 1)))
		if (string.ascii_letters.find(letras[i]) != - 1 and eh_consoante(letras[i])):
			lista_consoantes.append(letras[i])
			consoantes += 1

	print(lista_consoantes, consoantes)

main()
