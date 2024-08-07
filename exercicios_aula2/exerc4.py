import random

def exerc4():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    num_message = int(input("Quantas mensagens? "))
    message_size = int(input("Qual tamanho das mensagens? "))
    list_answer = []

    for a in range(num_message):
        message = ''
        for x in range(message_size):
            index = random.randint(0, len(symbols) - 1)
            message += symbols[index]
        
        list_answer.append(message)
    
    random.shuffle(list_answer)
    print("Sua lista aleatória: ", list_answer)

exerc4()