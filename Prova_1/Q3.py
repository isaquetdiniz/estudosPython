qteAlunosMaxima = 0;
qteAlunos = 0;
tabelaAlunos = {};
cadastrar = True;

while cadastrar and qteAlunosMaxima <= 200:
    matAluno = int(input('Insira a matrícula: '));
    if matAluno < 0:
        cadastrar = False;
        continue;
    nomeAluno = str(input('Insira o nome: '));
    idadeAluno = int(input('Insira a idade: '));
    if idadeAluno < 0:
        cadastrar = False;
        continue;
    tabelaAlunos[matAluno] = (nomeAluno, idadeAluno);
    qteAlunosMaxima += 1;

buscas = int(input('Insira o numero de buscas: '));
for i in range(0, buscas):
    idadeMin = int(input('Insira a idade minima: '));
    idadeMax = int(input('Insira a idade máxima: '));
    if idadeMin > idadeMax:
        print('Idade minima não pode ser maior do que a máxima!');
        continue;
    else:
        for i in tabelaAlunos:
            if tabelaAlunos[i][1] in range(idadeMin, idadeMax+1):
                qteAlunos += 1;
                print(i, tabelaAlunos[i]);

print(f'Foram encontrados {qteAlunos}')

