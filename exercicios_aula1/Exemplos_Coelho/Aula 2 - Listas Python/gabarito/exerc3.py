#!/usr/bin/env python
# coding: utf8

# 3) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def mostra_veredito(respostas_afirmativas):
	print("\n Veredito: ", end="") 
	if (respostas_afirmativas == 2):
		print("Suspeita")
	elif (respostas_afirmativas >= 3 and respostas_afirmativas <= 4):
		print("Cúmplice")
	elif (respostas_afirmativas == 5):
		print("Assassino")
	else:
		print("Inocente")

def faz_perguntas():
	perguntas = ["Telefonou para a vítima?" , "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
	respostas_afirmativas = 0
	for pergunta in perguntas:
		resposta = input(pergunta)
		if (resposta == "Sim" or resposta == "sim" or resposta == "SIM"):
			respostas_afirmativas += 1
	return respostas_afirmativas		

def main():
	respostas_afirmativas = faz_perguntas()
	mostra_veredito(respostas_afirmativas)		

main()
