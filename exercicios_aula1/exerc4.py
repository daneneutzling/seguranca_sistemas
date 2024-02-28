def jogo_da_forca(palavra_chave, num_tentativas, arquivo):
    # LISTA COM AS LETRAS DA PALAVRA CHAVE INFORMADA
    letras_palavra = list(palavra_chave.upper())

    # LISTA DE underlines PARA CADA LETRA DA PALAVRA CHAVE
    letras_adivinhadas = ['_' for _ in letras_palavra]
    
    # LETRAS INFORMADAS PELO USUÁRIO
    letras_tentadas = set()

    tentativas_usuario = 0

    print('Nº Tentativas: ', num_tentativas)
    interacoes = '\n' + 'Nº Tentativas: ' + str(num_tentativas)
    
    print('Palavra:', ''.join(letras_adivinhadas))
    interacoes += '\n' + 'Palavra:' + ''.join(letras_adivinhadas)
    #   ''.join(...)   =>   RETORNA OS ELEMENTOS DA LISTA SEM ESPAÇO E CARACTERES (COMO POR EXEMPLO: ['_', '_', '_'] )
    
    while tentativas_usuario < int(num_tentativas):
        letra_informada = input("Digite uma letra: ").upper()
        interacoes += '\n'+ ("Digite uma letra: " + letra_informada)

        if letra_informada == 'SAIR':
            print("Programa encerrado")
            interacoes += '\n'+ "Programa encerrado"

        if len(letra_informada) != 1 or not letra_informada.isalpha():
            print("Digite apenas uma letra válida")
            interacoes += '\n'+ "Digite apenas uma letra válida"
            continue

        if letra_informada in letras_tentadas:
            print("Letras já tentadas: ", letras_tentadas)
            interacoes += '\n'+ "Letras já tentadas: " + str(letras_tentadas)
            continue

        letras_tentadas.add(letra_informada)

        # SE A LETRA INFORMADA EXISTIR NA PALAVRA CHAVE
        if letra_informada in letras_palavra:

            # LOOP PERCORRE CADA LETRA DA PALAVRA CHAVE, SENDO QUE I = INDICE
            for i, letra in enumerate(letras_palavra):
            
                # SE A LETRA DO LOOP FOR IGUAL A LETRA INFORMADA
                if letra == letra_informada:
            
                    # ACESSA O ELEMENTO NA POSIÇÃO = I E TROCA O VALOR DELE PELA LETRA INFORMADA
                    letras_adivinhadas[i] = letra_informada

            # MOSTRA NA TELA A PALAVRA SENDO COMPLETADA
            print(''.join(letras_adivinhadas))
            interacoes += '\n' + (''.join(letras_adivinhadas))

        # CASO A LETRA NÃO ESTEJA NA PALAVRA CHAVE
        else:
            tentativas_usuario += 1
            tot_tentativas = int(num_tentativas) - tentativas_usuario
            print("Tente outra letra. Tentativas restantes: ", tot_tentativas)
            interacoes += '\n' + ("Tente outra letra. Tentativas restantes: " + str(tot_tentativas))


        if '_' not in letras_adivinhadas:
            print("Palavra Completada!")
            interacoes += '\n' + "Palavra Completada!"
            arquivo.write(interacoes)
            return
        
        elif int(num_tentativas) == tentativas_usuario:
            print("Tentativas esgotadas. A palavra era: " + palavra_chave)
            interacoes += '\n' + "Tentativas esgotadas. A palavra era: " + palavra_chave
            arquivo.write(interacoes)
            return
