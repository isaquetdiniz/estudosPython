'''
Questão referente à Lista de Exercícios de Repetição da Monitoria de Programação-I

Neste exercício, você irá criar uma calculadora que fará as operações de
soma, subtração, multiplicação e divisão entre dois números (float) X e Y. A
calculadora deverá imprimir uma mensagem de boas vindas ao ser iniciada, e uma
mensagem de que o programa está sendo encerrado. Você deverá ter um menu em
que o usuário possa escolher o tipo de operação que deseja executar (soma,
subtração, multiplicação ou divisão) ou se ele quer encerrar o programa.
Caso o usuário insira uma opção de operação não listada, imprima uma
mensagem de erro e peça para ele tentar novamente
'''

option = 0;
isContinue = True;
num1 = None;
num2 = None;

def messageWelcome():
    print('--------------------Calculadora PY--------------------');

def messageEnd():
    print('--------------------Encerrando Calculadora--------------------');

def selectOption():
    print('(1) - Soma | (2) - Substração | (3) - Multiplicação | (4) - Divisão | (5) - Sair\n');
    optionSelect = int(input('Selecione a opção desejada: '));
    return optionSelect;

def insertNumber():
    num1 = float(input('Insira o primeiro número: '));
    num2 = float(input('Insira o segundo número: '));
    return num1, num2;

def sum(num1, num2):
    return print(f'O resultado da soma entre {num1} e {num2} é {num1+num2}\n');

def sub(num1, num2):
    return print(f'O resultado da subtração entre {num1} e {num2} é {num1-num2}\n');

def mult(num1, num2):
    return print(f'O resultado da multiplicacao entre {num1} e {num2} é {num1*num2}\n');

def div(num1, num2):
    return print(f'O resultado da divisão entre {num1} e {num2} é {num1/num2}\n');


messageWelcome();

while isContinue:
    option = selectOption();

    if option == 1:
        num1, num2 = insertNumber();
        sum(num1, num2);
    elif option == 2:
        num1, num2 = insertNumber();
        sub(num1, num2);
    elif option == 3:
        num1, num2 = insertNumber();
        mult(num1, num2);
    elif option == 4:
        num1, num2 = insertNumber();
        div(num1, num2);
    elif option == 5:
        isContinue = False;
        continue;
    else:
        print('Opção inválida :(, tente novamente!\n');

messageEnd();




