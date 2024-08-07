def exerc5():
    
    cipher_text = '5 3 ‡ ‡ † 3 0 5 ) ) 6 * ; 4 8 2 6 ) 4 ‡ . ) 4 ‡ ) ; 8 0 6 * ; 4 8 † 8 ¶ 6 0 ) ) 8 5 ; ; ] 8 * ; : ‡ * 8 † 8 3( 8 8 ) 5 * † ; 4 6 ( ; 8 8 * 9 6 * ? ; 8 ) * ‡ ( ; 4 8 5 ) ; 5 * † 2 : * ‡ ( ; 4 9 5 6 * 2 ( 5 * - 4 ) 8 ¶ 8 *;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;'
    
    cipher_text = cipher_text.replace(' ', '')

    count_symbol = {}

    for symbol in cipher_text:
        if symbol not in count_symbol:
            count_symbol[symbol] = 1
        else:
            count_symbol[symbol] += 1

    count_symbol = sorted(count_symbol.items(), key=lambda x: x[1], reverse=True)
    
    for symbol, count in count_symbol:
        print(f"'{symbol}' : '{count}'")
        
    clear_text =cipher_text.replace('8','e')
    clear_text = clear_text.replace(';','t')
    clear_text = clear_text.replace('4','h')
    clear_text = clear_text.replace(')','s')
    clear_text = clear_text.replace('‡','o')
    clear_text = clear_text.replace('*','n')
    clear_text = clear_text.replace('5','a')
    clear_text = clear_text.replace('6','i')
    clear_text = clear_text.replace('(','r')
    clear_text = clear_text.replace('†','d')
    clear_text = clear_text.replace('1','f')
    clear_text = clear_text.replace('0','l')
    clear_text = clear_text.replace('2','b')
    clear_text = clear_text.replace('9','m')
    clear_text = clear_text.replace('3','g')
    clear_text = clear_text.replace(':','y')
    clear_text = clear_text.replace('?','u')
    clear_text = clear_text.replace('¶','v')
    clear_text = clear_text.replace('.','p')
    clear_text = clear_text.replace(']','w')
    clear_text = clear_text.replace('-','c')
    
    print(clear_text)

exerc5()