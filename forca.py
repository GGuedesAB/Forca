import getpass  # Importando bible (Descobrir pra que serve)
play_again = True
while play_again:
    secret_word = getpass.getpass(prompt='Digite a palavra secreta: ')  # getpass.getpass(prompt" ") é igual input, porém o que o user digita fica escondido
    counter = 0
    repeated_letter = []  # Deve ser lista, pois string não é alteravel
    position = 0  # Começa em 0 porque ao entrar a letra ele já incrementa
    list1 = []  # é utilizado para informar as posições, ex.: [1,4,5]
    i = 0  # indice(n° da posição onde está)
    life = (len(secret_word) // 2) + 1  # n° de vidas = tamanho da palavra divido por 2 (arredonando pra baixo) + 1  

    print(f'Total de chances: ',end = '')
    print("* "*life)

    print('_ '*len(secret_word))  

    while True:  # De qualquer forma o if counter == len vai breakar o programa
        cased_letter = input('Digite uma letra: ')  # Essa variavel cased_letter serve para passar a letra em minusculo
        letter = cased_letter.lower()

        if len(cased_letter)>1:
            print('Digite apenas uma letra')
            continue

        if letter in secret_word and len(secret_word) != counter and secret_word.count(letter)==1 and letter not in repeated_letter:
            for index in secret_word:  # Nesse if é a verificação de quando só tem uma letra daquela na palavra
                position+=1
                if index==letter.lower():
                    break
            print(f'A letra {letter} aparece na palavra {secret_word.count(letter)} vezes, na posição {position}')
            position = 0
            counter+=1
        
        elif letter in secret_word and len(secret_word) != counter and secret_word.count(letter)>1 and letter not in repeated_letter:
            for index1 in secret_word:  # Nesse elif é a verificação quando tem mais de uma letra daquela na palavra
                position+=1
                if index1==letter and i!=secret_word.count(letter):
                    list1.insert(i,position)
                    i+=1
                elif i==secret_word.count(letter):
                    break
            print(f'A letra {letter} aparece na palavra {secret_word.count(letter)} vezes, nas posições {list1}')
            counter+=secret_word.count(letter)
            list1 = []  
            position = 0
            i = 0
        
        else:
            if letter in repeated_letter:  # Essa opção não gasta vida, pois já foi perdida uma vida anteriormente
                print("Digite outra letra, essa já foi ultilizada.")  
            else:  # Essa opção gasta vida
                print('A palavra não possui essa letra.')
                life-=1
                print(f'Total de chances: ',end = '')
                print("* "*life)
                
        repeated_letter.append(letter)  # Adicionando a letra que acabou de ser colocada no repeated_letter para não usa-la de novo

        if counter == len(secret_word) or life==0:  # Vai ser if, porque precisa que entre nessa condição
            if life==0:
                print("\n", "GAME-OVER", "\n")
            break  # Encontrou a palavra inteira
    
    if life != 0:    
        print(f'{secret_word}')
        print("Parabéns você conseguiu")
    
    print()

    y_or_no = input("Deseja jogar novamente? s/n ")
    
    if y_or_no is "s" or y_or_no is "S":
        play_again = True
    
    else:
        play_again = False

    
