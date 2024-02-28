def verifica_num_primo(arquivo):
    elemento_input = int(input("Digite um número: "))
    interacoes = '\n' + ("Digite um número: " + str(elemento_input))

    if elemento_input is None or elemento_input == '':
        print("Argumento inválido")
        interacoes += '\n' + "Argumento inválido"

    try:
        elemento = int(elemento_input)
    except ValueError:
        print("O valor deve ser numérico")
        interacoes += '\n' + "O valor deve ser numérico"

    tot_divisao = 0

    # LOOP ATÉ O VALOR INFORMADO, TESTANDO SE OS NÚMEROS DIVIDEM O ELEMENTO (DE FORMA INTEIRA), CASO SIM, ADD 1 PARA A VARIAVEL
    # range(1, elemento + 1) gera uma sequencia do 1 até o valor do elemento (elemento + 1 é usado para incluir o valor do elemento)
    for a in range(1, elemento + 1):
        if elemento % a == 0:
            tot_divisao += 1

    if tot_divisao == 2:
        resultado = "True"

    else:
        resultado = "False"
    
    print(resultado)
    interacoes += '\n' + resultado
    arquivo.write(interacoes)