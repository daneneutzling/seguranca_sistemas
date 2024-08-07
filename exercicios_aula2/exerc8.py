def exerc8():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = 'explanation'
    key = 'leg'
    answer = ''

    text = text.upper()
    key = key.upper()

    while len(key) < len(text):
        for letter in key: 
            if len(key) < len(text):
                key += letter
    
    key = key[:len(text)]

    while len(answer) < len(text):
        for text_letter, text_key in zip(text, key):
            index_text = symbols.find(text_letter)
            index_key  = symbols.find(text_key)

            index_answer = index_text + index_key

            if index_answer >= 26:
                index_answer = index_answer - 26
            
            answer_letter = symbols[index_answer]
            answer += answer_letter
        
    print(answer) 
    
exerc8()