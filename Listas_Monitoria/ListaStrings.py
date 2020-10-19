'''
Lista da monitoria de strings de Programação - I
'''

def question1():
    biggestWord = '';

    inputedString = str(input('Insira uma string:'));

    splitedString = inputedString.split();

    for word in splitedString:
        if len(word) > len(biggestWord):
            biggestWord = word;

    print(f'A maior palavra é {biggestWord}');

def question2():
    ocurrencyChar = 0;

    inputedPhase = str(input('Insira uma frase: '));
    inputedChar = str(input('Insira uma letra: '));

    ocurrencyChar = inputedPhase.count(inputedChar);

    print(f'A letra {inputedChar} apareceu {ocurrencyChar} vezes');

def question3():

    inputedWord = str(input('Insira uma palavra: '));
    reversedWord = ''.join(reversed(inputedWord));

    if inputedWord == reversedWord:
        print(f'{inputedWord} é um palíndromo');
    else:
        print(f'{inputedWord} não é um palíndromo');

def question4():
    newWord = [];

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

    inputedWord = str(input('Palavra: '));

    newWord = [str(ord(chr)+3) for chr in inputedWord]
    print(''.join(newWord));

question4()


