#!/usr/bin/env python
# coding: utf8

#1) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def main():
	#ler as 4 notas
	notas = lerNotas()
	#calcular a média
	media = calcularMedia(notas)
	#mostrar os resultados
	mostraResultados(notas, media)
	
	
def lerNotas():
	notas = []
	for i in range(4):
		nota = float(input('Informe a nota ' + str(i + 1) + ':'))
		notas.append(nota)	
	return notas

def calcularMedia(notas):
	soma = 0
	for nota in notas:
		soma += nota
	return soma/len(notas)	

def mostraResultados(notas, media):
	for i in range(len(notas)):
		print('Nota', (i + 1), notas[i])
	print('Média', media)	
	
main()	
