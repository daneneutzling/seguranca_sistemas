def calcular_media_ponderada(arquivo):
    lista_valores = str(input("Informe uma lista de valores: "))
    interacoes = '\n' + ("Informe uma lista de valores: " + lista_valores)
    
    if lista_valores.lower() == 'sair':     
        print("Programa encerrado.")
        interacoes += '\n' + "Programa ecerrado."

    if lista_valores is None or lista_valores == '':
        print("A lista não pode ser nula.")
        interacoes += '\n' + "A lista não pode ser nula."

    try:
        lista_valores = list(map(float, lista_valores.split(',')))
    except ValueError:
        print("A lista deve ser numérica.")
        interacoes += '\n' + "A lista deve ser numérica."

    lista_pesos = str(input("Informe uma lista de pesos: "))
    interacoes += '\n' + ("Informe uma lista de pesos: " + lista_pesos)

    if lista_pesos.lower() == 'sair':    
        print("Programa encerrado.")
        interacoes += "Programa ecerrado."

    if lista_pesos is None or lista_pesos == '':
        print("A lista não pode ser nula.")
        interacoes += "A lista não pode ser nula."

    try:
        lista_pesos = list(map(float, lista_pesos.split(',')))
    except ValueError:
        print("A lista deve ser numérica.")
        interacoes += "A lista deve ser numérica."

    if len(lista_valores) == len(lista_pesos):
        soma_valores_pesos = 0
        soma_pesos = 0        

        # range(len(lista_valores)) => cria uma sequencia de numero de acordo com o tamanho da lista
        for i in range(len(lista_valores)):
            soma_valores_pesos += lista_valores[i] * lista_pesos[i]
            soma_pesos += lista_pesos[i]

        tot_media = round(soma_valores_pesos / soma_pesos, 2)
        resultado = "Total da Média Ponderada: " + str(tot_media)
        interacoes += '\n' + str(resultado)

    else:
        resultado = 'As listas não possuem a mesma quantidade de informações...'
        interacoes += '\n' + str(resultado)

    print(resultado)
    arquivo.write(interacoes)