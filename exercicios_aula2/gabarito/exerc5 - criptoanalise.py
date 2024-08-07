texto_cifrado = '53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;'

#remove espaços em branco
texto_cifrado = texto_cifrado.replace(' ', '').strip()

#conta o número de ocorrências de cada símbolo
contador_simbolos = {}

for i in range(len(texto_cifrado)):
	contador_simbolos[texto_cifrado[i]] = 0
	
for simbolo in texto_cifrado:
	contador_simbolos[simbolo] += 1	
	
simbolos_ordenados = sorted(contador_simbolos.items(), key=lambda kv: kv[1])
for simbolo in simbolos_ordenados:
	print(simbolo[0],'=',simbolo[1])

'''
. = 1
] = 1
- = 1
¶ = 2
  = 3
? = 3
3 = 4
: = 4
2 = 5
9 = 5
0 = 6
1 = 7
† = 8
( = 9
6 = 11
5 = 12
* = 14
‡ = 15
) = 16
4 = 19
; = 27
8 = 34
'''

# conta quantas vezes cada um dos simbolos mais achados se repete em sequência
oito = texto_cifrado.count('88')
ponto_virgula = texto_cifrado.count(';;')
quatro = texto_cifrado.count('44')
print('\n','8 -', oito) # 5 vezes
print('; -', ponto_virgula) # 1 vez
print('4 -', quatro) # nenhuma vez

#procura pela ocorrencias do THE
texto_claro = texto_cifrado.replace('8','e')
texto_claro = texto_claro.replace(';','t')
texto_claro = texto_claro.replace('4','h')

#E, T, A, O, I, N, S, H, R, D, L
texto_claro = texto_claro.replace(')','s')
texto_claro = texto_claro.replace('‡','o')
texto_claro = texto_claro.replace('*','n')
texto_claro = texto_claro.replace('5','a')
texto_claro = texto_claro.replace('6','i')
texto_claro = texto_claro.replace('3','g')
texto_claro = texto_claro.replace('†','d')
texto_claro = texto_claro.replace('0','l')
texto_claro = texto_claro.replace('2','b')
texto_claro = texto_claro.replace('.','p')
texto_claro = texto_claro.replace('¶', 'd')
texto_claro = texto_claro.replace(']', 'w')
texto_claro = texto_claro.replace(':', 'y')
texto_claro = texto_claro.replace('(','r')
texto_claro = texto_claro.replace('9', 'm')
texto_claro = texto_claro.replace('?','u')
texto_claro = texto_claro.replace('-','c')
texto_claro = texto_claro.replace('1', 'f')

print('\n',texto_claro)
