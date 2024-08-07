def exerc6():
    matriz = [['M', 'F', 'H', 'I/J', 'K'],
              ['U', 'N', 'O', 'P', 'Q'],
              ['Z', 'V', 'W', 'X', 'Y'],
              ['E', 'L', 'A', 'R', 'G'],
              ['D', 'S', 'T', 'B', 'C'] ]

    clear_text = 'Must see you over Cadogan West. Coming at once'

    clear_text = clear_text.upper().replace('J', 'I').replace(' ', '')

    print(clear_text)




exerc6()