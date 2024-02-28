def verifica_num_primo_arq(nome_arquivo):
    # DEFINO QUE A VARIAVEL POSSUI O NOME DO ARQUIVO QUE IREI ACESSR
    arquivo = nome_arquivo + '.txt' 
    try: 
        # TENTO ABRIR O ARQUIVO E O CHAMO DE OBJETO
        with open(arquivo) as objeto: 
            # CHAMO O MÉTODO readlines() NO OBJETO PARA LER LINHA A LINHA DO ARQUIVO E MANDO OS DADOS PARA UMA VARIAVEL
            dados = objeto.readlines()
    except FileNotFoundError: 
        # CASO NÃO CONSIGA ENCONTRAR O ARQUIVO, ERRO NA TELA
        return print('O arquivo ' + arquivo + ' não foi encontrado') 

    # FAÇO UM LOOP DOS DADOS
    for a in dados:
        try:    
            # TENTO PEGAR O VALOR ATUAL E JOGÁ-LO PARA UMA VARIÁVEL NUMBER
            numero_input = int(a)
        except ValueError:
            # CASO O VALOR DO DADO NÃO SEJA NUMÉRICO, ERRO NA TELA
            print("Os valores devem ser apenas numéricos")

        tot_divisores = 0

        # LOOP ATÉ O VALOR INFORMADO, TESTANDO SE OS NÚMEROS DIVIDEM O numero_input (DE FORMA INTEIRA), CASO SIM, ADD 1 PARA A VARIAVEL
        # range(1, numero_input + 1) gera uma sequencia do 1 até o numero_input (numero_input + 1 é usado para incluir o valor do numero_input)
        for i in range(1, numero_input + 1):
            if numero_input % i == 0:
                tot_divisores += 1

        if tot_divisores == 2:
            print(f"{numero_input} = Número Primo")
        else:
            print(f"{numero_input} = NÃO é número Primo")

verifica_num_primo_arq("dados_exerc6")