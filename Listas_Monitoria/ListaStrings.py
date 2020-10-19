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
    continueEncrypt = True;

    letters = ['abcdefghijklmnopqrstuvxwyz']
    numbers = ['123456789'];

    inputedWord = str(input('Palavra: '));

    def encrypt(chr):
        position = letters.find(chr) + 3;
        if position >= len(letters):
            position -= len(letters);


    newWord = [encrypt(chr) for chr in inputedWord if chr in letters]

question4()


