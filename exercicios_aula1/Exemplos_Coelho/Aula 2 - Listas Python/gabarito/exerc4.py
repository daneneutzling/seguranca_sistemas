#!/usr/bin/env python
# coding: utf8

'''
4) Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
 "Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 

O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos 
concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

SO                 	  Votos   %
-------------------   -----  ---
Windows Server  	  1500   17%
Unix                  3500   40%
Linux                 3000   34%
Netware                500    5%
Mac OS                 150    2%
Outro                  150    2%
-------------------   -----  --- 
Total                 8800
O SO mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

def main():
	mostra_opcoes()
	respostas = faz_pesquisa()
	mostra_resultados(respostas, respostas[6])

def mostra_opcoes():
	print("As possíveis respostas são: ")
	print("1 - Windows Server ")
	print("2 - Unix")
	print("3 - Linux")
	print("4 - Netware")
	print("5 - Mac OS")
	print("6 - Outro")

def mostra_resultados(respostas, total):
	print("---------------------------") 
	print("SO \t Votos \t %")
	print("---------------------------") 
	print("Windows \t %d \t %d%%" % (respostas[0], respostas[0] / total * 100))
	print("Unix \t %d \t %d%%" % (respostas[1], respostas[1] / total * 100)) 
	print("Linux \t %d \t %d%%" % (respostas[2], respostas[2] / total * 100))
	print("Netware \t %d \t %d%%" % (respostas[3], respostas[3] / total * 100))
	print("Mac OS \t %d \t %d%%" % (respostas[4], respostas[4] / total * 100))
	print("Outro \t %d \t %d%%" % (respostas[5], respostas[5] / total * 100))
	print("---------------------------") 
	print("Total \t %d" % total)

def faz_pesquisa():
	respostas = [0, 0, 0, 0, 0, 0, 0] #o último índice armazena o número total
	opcao = int(input("Qual o melhor Sistema Operacional para uso em servidores?"))
	while (opcao != 0):
		respostas[6] += 1
		respostas[opcao - 1] += 1
		opcao = int(input("Qual o melhor Sistema Operacional para uso em servidores?"))
	return respostas

main()
