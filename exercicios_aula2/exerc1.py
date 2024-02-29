def exerc1():
    action = ""

    while action != 'EXIT':
        action = input("Do you wish to encrypt or decrypt a message or exit?").upper()
        messsage = input("Enter youor message:").upper()
        key = int(input("Enter the key number (1-52): "))

        if action == 'ENCRYPT':
            answer = "Your translated text is: " + asnwer_cripto

        else:
            answer = "Your translated text is: " + asnwer_cripto

# Do you wish to encrypt or decrypt a message or exit?
# encrypt
# Enter your message:
# The sky above the port was the color of television, tuned to a dead channel.
# Enter the key number (1-52)
# 13
# Your translated text is:
# gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.
# Do you wish to encrypt or decrypt a message or exit?
# decrypt
# Enter your message:
# gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.
# Enter the key number (1-52)
# 13
# Your translated text is:
# The sky above the port was the color of television, tuned to a dead channel.
# Do you wish to encrypt or decrypt a message or exit?
# exit