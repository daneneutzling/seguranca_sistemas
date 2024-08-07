def exerc1():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    action = ""
    answer = ""

    while action != 'EXIT':
        action = input("Do you wish to encrypt or decrypt a message or exit?").upper()
        message = input("Enter your message:")
        key = int(input("Enter the key number (1-52): "))
        answer = ""

        for symbol in message: # simbolo na mensagem 
            if symbol in symbols: # simbolo na lista de simbolos
                index = symbols.find(symbol) # pega o simbolo em destaque e procura ele na lista de simbolos, joga pra variavel
                    
                if action == 'ENCRYPT': # se for isso, soma o index atual com a chave
                    indexAnswer = index + key
                elif action == "DECRYPT": # se for isso, diminui o valor do index com a chave
                    indexAnswer = index - key

                if indexAnswer >= len(symbols): # ve se o valor do index ta acima do tamanho da lista de simbolos
                    indexAnswer = indexAnswer - len(symbols) # se ta maior, ele diminui
                elif indexAnswer < 0:
                    indexAnswer = indexAnswer + len(symbols) # se ta menor, ele soma

                answer = answer + symbols[indexAnswer] # concatena o que já tem com o simbolo da lista, de acordo com o index

            else:
                answer = answer + symbol # caso o simbolo que o usuario digitou nao exista na lista de simbolo, nao faz nada, apenas junta

        print("Your translated text is: " + answer)

exerc1()