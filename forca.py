secret_word = input('Digite a palavra secreta: ')
counter = 0
repeated_letter = ''
position = 0
list1 = [0,0]
i = 0

while True:
    letter = input('Digite uma letra: ')

    if letter in secret_word and len(secret_word) != counter and secret_word.count(letter)==1 and letter not in repeated_letter:
        for index in secret_word:
            position+=1
            if index==letter:
                break

        print(f'A letra {letter} aparece na palavra {secret_word.count(letter)} vezes, na posição {position}')
        position = 0
        counter+=1

    elif letter in secret_word and len(secret_word) != counter and secret_word.count(letter)>1 and letter not in repeated_letter:
        for index1 in secret_word:
            position+=1
            if index1==letter and i!=secret_word.count(letter):
                list1.insert(i,position)
                i+=1
            elif i==secret_word.count(letter):
                break

        print(f'A letra {letter} aparece na palavra {secret_word.count(letter)} vezes, nas posições {list1}')
        counter+=secret_word.count(letter)

    if counter == len(secret_word):
        break
    else:
        print('A palavra não possui essa letra')
        continue

print("Parabéns você conseguiu")
# TODO: VERIFICAR SE O CÓDIGO ESTÁ RODANDO PERFEITAMENTE, COLOCAR UM MECANISMO DE CHANCES QUE O USUÁRIO TEM
# TODO: COLOCAR UM MECANISMO DE REPETIÇÃO PARA ASSIM QUE O JOGO TERMINAR PERGUNTAR SE QUER REPETIR
# TODO: ADICIONAR ESPAÇO ENTRE "letra" e "{letter}"
# TODO: PARA CADA PALAVRA INSERIDA, VERIFICAR SE A PALAVRA FOI DESCOBERTA
    # EXPLANATION: QUANDO EU TERMINO A PALAVRA, EU PRECISO INSERIR MAIS UMA LETRA PARA O PROGRAMA ENTENDER QUE ACERTEI A PALAVRA