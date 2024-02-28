#!/usr/bin/env python
# coding: utf8

#Faça uma função que, dado um total de segundos, calcule o total de horas, minutos e  segundos. 

def total(tempo):
	tempo = int(tempo)
	horas =  int(tempo / 3600)
	minutos = int((tempo - (3600 * horas)) / 60)
	segundos = int(tempo - 3600 * horas - minutos * 60)
	print(str(horas) + ":" + str(minutos) + ":" + str(segundos))

def main():
	tempo = input("Qual a quantidade de segundos total?")
	total(tempo)
	
main()
