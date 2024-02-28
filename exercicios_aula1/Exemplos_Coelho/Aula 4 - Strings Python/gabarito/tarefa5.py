#!/usr/bin/env python
# coding: utf8


__AUTHOR__ = "Rafael Vieira Coelho"
__DATE__ = "31/03/2019"

''' Modifique a função encontrar de modo que ela receba um terceiro parâmetro,
o índice da string por onde ela deve começar sua procura.'''

def encontrar(palavra, letra):
	indice = 0
	while indice < len(palavra):
		if palavra[indice] == letra:
			return indice
		indice = indice + 1
	return -1

def encontrar2(palavra, letra, pos_inicial):
	indice = pos_inicial
	while indice < len(palavra):
		if palavra[indice] == letra:
			return indice
		indice = indice + 1
	return -1

def main():
	palavra = input("Qual a palavra?")
	letra = input("Qual a letra a ser procurada?")
	posicao_inicial = int(input("Qual a posição inicial?"))
	posicao = encontrar2(palavra, letra, posicao_inicial)
	if (posicao == -1):
		print("Não foi encontrada")
	else:
		print("Indice: " + str(posicao))	

main()				
