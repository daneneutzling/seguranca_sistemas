import random

def exerc3():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    num_message = 5
    message_size = 10
    list_answer = []

    for a in range(num_message):
        message = ''
        for x in range(message_size):
            index = random.randint(0, len(symbols) - 1)
            message += symbols[index]
        
        list_answer.append(message)
    
    random.shuffle(list_answer)
    print(list_answer)

exerc3()