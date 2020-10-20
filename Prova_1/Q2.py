numeros = [];
isContinue = True;
quantidadeNumeros = 0;
maiorMultiplo11 = -10 ** 20;

while isContinue:
    numero = int(input('Insira um numero negativo: '));
    if numero >= 0 and quantidadeNumeros <= 300:
        isContinue = False;
        continue;
    else:
        quantidadeNumeros += 1;
        numeros.append(numero);

multiplosDeCinco = [numero for numero in numeros if (numero % 5 == 0)];
multiplosDeCinco.reverse();

for numero in numeros:
    if (numero % 11 == 0) and numero > maiorMultiplo11:
        maiorMultiplo11 = numero;

if maiorMultiplo11 == -10 ** 20:
    maiorMultiplo11 = 'Não existe';

print(multiplosDeCinco);
print(maiorMultiplo11);



