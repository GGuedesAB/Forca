import getpass
secret_word = getpass.getpass(prompt='Digite a palavra secreta: ')
counter = 0
repeated_letter = ''
position = 0  # Começa em 0 porque ao entrar a letra ele já incrementa
list1 = []
i = 0

while True:  # De qualquer forma o if counter == len vai breakar o programa
    letter = input('Digite uma letra: ')

    if letter in secret_word and len(secret_word) != counter and secret_word.count(letter)==1 and letter not in repeated_letter:
        for index in secret_word:
            position+=1
            if index==letter:
                break

        print(f'A letra {letter} aparece na palavra {secret_word.count(letter)} vezes, na posição {position}')
        position = 0
        counter+=1
        list1 = []
        
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
        list1 = []
        position = 0
        i = 0
    else:
        print('A palavra não possui essa letra')
        continue

    if counter == len(secret_word):  # Vai ser if, porque precisa que entre nessa condição
        break  # Encontrou a palavra inteira


print("Parabéns você conseguiu")
# TODO: VERIFICAR SE O CÓDIGO ESTÁ RODANDO PERFEITAMENTE, COLOCAR UM MECANISMO DE CHANCES QUE O USUÁRIO TEM
# TODO: COLOCAR UM MECANISMO DE REPETIÇÃO PARA ASSIM QUE O JOGO TERMINAR PERGUNTAR SE QUER REPETIR
