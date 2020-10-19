'''
Primeira questão da prova antiga de Fernando

Questão 1:
Faça um programa Python para calcular a soma dos N primeiros termos da série abaixo. O
valor de N deve ser lido no início e deve ser positivo. Imprimir o resultado da seguinte forma:
“O valor da série com ... termos é ...”.
S = 10 / 1 – 12 / 5 + 14 / 8 – 16 / 11 + 18 / 15 – 20 / 17 + ...
'''
termoNumerador = 10;
termoDenominador = 1;
somaDosTermos = 0;

def geraNumeradores(numerador, n):
    if(n == 0):
        return numerador;
    numerador += 2;
    return numerador;

def geraDenominadores(denominador, n):
    if(n == 1):
        denominador += 4;
        return denominador;
    elif(n == 0):
        return denominador;
    else:
        denominador += 3;
        return denominador;

n = int(input('Insira um número inteiro positivo:'));

for i in range(1, n):
    termoNumerador = geraNumeradores(termoNumerador, i-1);
    termoDenominador = geraDenominadores(termoDenominador, i-1);
    termoNumerador2 = geraNumeradores(termoNumerador, i);
    termoDenominador2 = geraDenominadores(termoDenominador, i);
    print(f'{termoNumerador}/{termoDenominador} - {termoNumerador2}/{termoDenominador2}');
    termoOperacao = termoNumerador/termoDenominador - termoNumerador2/termoDenominador2;
    somaDosTermos += termoOperacao;

print(f'O valor da série com {n} termos é {somaDosTermos}');

