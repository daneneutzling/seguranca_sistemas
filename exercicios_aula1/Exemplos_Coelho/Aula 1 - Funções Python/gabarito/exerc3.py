#!/usr/bin/env python
# coding: utf8

import math

def main():
	print("Informe o angulo: ")
	angulo = float(input())	
	calculo(angulo)

def calculo(angulo):
	print("O seno do ângulo ", angulo, " é ", math.sin(angulo))
	print("O cosseno do ângulo ", angulo, " é ", math.cos(angulo))
	print("A tangente do ângulo ", angulo, " é ", math.tan(angulo))
	
main()	
