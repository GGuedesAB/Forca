secret_word = input('Digite a palavra secreta: ')
enter_pass = True
counter = 0
repeated_letter = ''
position = 1
list1 = [0,0]
i = 0

while enter_pass:
    letter = input('Digite uma letra: ')

    # Aqui tem um bug
    #   Quando entramos a última letra, devemos primeiro verificar SE ELA ESTÁ NA PALAVRA antes de fazer isso:
    if counter == len(secret_word):
        enter_pass = False

    elif letter in secret_word and len(secret_word) != counter and secret_word.count(letter)==1 and letter not in repeated_letter:
        for index in secret_word:
            position+=1
            if index==letter:
                break
        # Adicionar um espaço entre "letra" e "{letter}"
        print(f'A letra{letter} aparece na palavra {secret_word.count(letter)} vezes, na posição {position}')
        position = 0
        counter+=1

    elif letter in secret_word and len(secret_word) != counter and secret_word.count(letter)>1 and letter not in repeated_letter:
        for index1 in secret_word:
            position+=1
            if index1==letter and i!=secret_word.count(letter):
                insert.list1(i,position)
                i+=1
            elif i==secret_word.count(letter):
                break
        # Adicionar um espaço entre "letra" e "{letter}"
        print(f'A letra{letter} aparece na palavra {secret_word.count(letter)} vezes, nas posições {lis1}')
        counter+=secret_word.count(letter)

    else:
        print('A palavra não possui essa letra')
        continue

print("Parabéns você conseguiu")
# TODO: VERIFICAR SE O CÓDIGO ESTÁ RODANDO PERFEITAMENTE, COLOCAR UM MECANISMO DE CHANCES QUE O USUÁRIO TEM
# TODO: COLOCAR UM MECANISMO DE REPETIÇÃO PARA ASSIM QUE O JOGO TERMINAR PERGUNTAR SE QUER REPETIR
# DICAS:
#   A variável enter_pass não é necessária