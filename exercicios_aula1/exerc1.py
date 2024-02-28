def busca_elemento(lista, elemento, index):
    if index >= len(lista):
        return False

    if lista[index] == elemento:
        return True
    return busca_elemento(lista, elemento, index + 1)
    
def exercicio1(arquivo):
    lista_input = str(input("Informe uma lista de números: "))
    interacoes = '\n' + "Informe uma lista de números: " + lista_input

    if lista_input.lower() == 'sair':       
        print("Programa encerrado.")
        interacoes += '\n' + "Programa encerrado."
        
    elif lista_input is None or lista_input == '':
        print("A lista não pode ser nula.")
        interacoes += '\n' + "A lista não pode ser nula."

    try:
        lista = list(map(int, lista_input.split(',')))
    except ValueError:
        print("A lista deve ser numérica.")
        interacoes += '\n' + "A lista deve ser numérica."

    elemento_input = str(input("Informe o elemento a ser procurado na lista: "))
    interacoes += '\n' + "Informe o elemento a ser procurado na lista: " + elemento_input

    if elemento_input.lower() == 'sair':    
        print("Programa encerrado.")
        interacoes += '\n' + "Programa encerrado."
    
    elif elemento_input is None or elemento_input == '':
        print("O elemento não pode ser nulo.")
        interacoes += '\n' + "O elemento não pode ser nulo."

    try:
        elemento = int(elemento_input)
    except ValueError:
        print("O elemento deve ser numérico.")
        interacoes += '\n' + "O elemento deve ser numérico."
    
    lista_ordenada = sorted(lista)

    resultado = str(busca_elemento(lista_ordenada, elemento, 0))

    print(resultado)
    interacoes += '\n' + resultado

    arquivo.write(interacoes)