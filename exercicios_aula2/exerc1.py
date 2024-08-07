def exerc1():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    action = ""
    answer = ""

    while action != 'EXIT':
        action = input("Do you wish to encrypt or decrypt a message or exit?").upper()
        message = input("Enter your message:")
        key = int(input("Enter the key number (1-52): "))
        answer = ""

        for symbol in message: 
            if symbol in symbols:
                index = symbols.find(symbol) 
                
                if action == 'ENCRYPT': 
                    indexAnswer = index + key
                elif action == "DECRYPT":
                    indexAnswer = index - key

                if indexAnswer >= len(symbols): 
                    indexAnswer = indexAnswer - len(symbols) 
                elif indexAnswer < 0:
                    indexAnswer = indexAnswer + len(symbols) 

                answer = answer + symbols[indexAnswer] 

            else:
                answer = answer + symbol 
                
        print("Your translated text is: " + answer)

exerc1()