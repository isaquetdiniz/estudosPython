### Primeira Questão da Prova de Programação I com Fernando
### Estudante: Isaque Teixeira Diniz 
### Curso: Sistemas de Informação

numeradorInicialSequencia = 150;
denominadorInicialSequencia = 20;

numeradores=[];
denominadores=[];

n = int(input('Insira um inteiro positivo para N: '));

while n < 0:
    n = int(print('Insira um inteiro positivo para N: '));

def geraNumeradores(numeradorInicial, n):
    if n % 2 == 0:
        numeradorInicial += 14*n
        return numeradorInicial;
    else:
        numeradorInicial += 6*n
        return numeradorInicial;

def geraDenominadores(denominadorInicial, n):
    denominadorInicial += 10*n;
    return denominadorInicial;

for i in range(0, n):
    numeradores.append(geraNumeradores(numeradorInicialSequencia, i));
    denominadores.append(geraDenominadores(denominadorInicialSequencia, i));

print(numeradores);
print(denominadores);
