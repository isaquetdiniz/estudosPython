'''
Questão 2 da Prova Antiga de Fernando

Faça um programa Python para ler uma seqüência de números inteiros – a leitura pára
quando o número zero for lido. O programa deve imprimir as seguintes informações como
resultado (nesta ordem):

• A quantidade total de números digitados.
• Os números lidos cujos valores têm 3 dígitos significativos. A impressão destes números
deve mostrar primeiro os números negativos (de 3 dígitos) na ordem em que foram lidos
e depois os positivos (idem).
• A média aritmética dos números impressos no item anterior.
• O maior número lido que seja múltiplo de 7.

OBS: Não pode usar as funções len e sum.
'''

print('----------Questão 2------------');
print('Insira uma sequência de números inteiros - para parar, insira 0\n');

continuar = True;
numeros = [];
numerosTresDigitos = [];
numerosTresDigitosPositivos = [];
numerosTresDigitosNegativos = [];
mediaNumerosTresDigitos = 0;
maiorMultiploSete = 0;

while continuar:
    numeroDigitado = int(input('Insira um numero inteiro: '));
    if numeroDigitado == 0:
        continuar = False;
        continue;
    numeros.append(numeroDigitado);

numerosTresDigitosPositivos = [numero for numero in numeros if (numero > 99)];
numerosTresDigitosNegativos = [numero for numero in numeros if (numero < -99)];
numerosTresDigitos = [numero for numero in numeros if (numero > 99) or (numero < -99)];

qteNumeros = len(numerosTresDigitos)-1;
somaNumeros = 0;
for numero in numerosTresDigitos:
    somaNumeros += numero;

mediaNumerosTresDigitos = (somaNumeros/qteNumeros);

for numero in numeros:
    if (numero % 7 == 0) and abs(numero) > maiorMultiploSete:
        maiorMultiploSete = numero;

print(f'A quantidade de numeros digitados foi {len(numeros)}');
print(f'Os numeros de 3 digítos positivos são: {numerosTresDigitosPositivos}');
print(f'Os numeros de 3 digítos negativos são: {numerosTresDigitosNegativos}');
print(f'A media dos números de 3 digitos é {mediaNumerosTresDigitos}');
print(f'O maior múltiplo de 7 é {maiorMultiploSete}');
