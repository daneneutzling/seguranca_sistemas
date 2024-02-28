import exerc1
import exerc2
import exerc3
import exerc4

def main():
    arquivo = open('interacoes_usuario.txt', "w")

    print("ATIVIDADES")
    print("1 - Buscar Elemento em um Lista;")
    print("2 - Verificar Número Primo;")
    print("3 - Calcular Média Ponderada;")
    print("4 - Jogo da Forca.")
    escolha_input = str(input("Escolha uma das atividades: "))
    arquivo.write("Atividade escolhida: " + escolha_input)

    if escolha_input.lower() == 'sair':    # CASO O USUÁRIO QUEIRA ENCERRAR O PROGRAMA
        return print("Programa encerrado.")
    
    if escolha_input is None or escolha_input == '':
        main()

    try:
        escolha = int(escolha_input)
    except ValueError:
        main()

    if escolha == 1:
        exerc1.exercicio1(arquivo)
        
    elif escolha == 2:
        exerc2.verifica_num_primo(arquivo)
    
    elif escolha == 3:
        exerc3.calcular_media_ponderada(arquivo)
    
    elif escolha == 4:
        exerc4.jogo_da_forca('SEGURANÇA', '5', arquivo)

main()