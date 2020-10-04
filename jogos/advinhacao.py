import random;

def jogar():

    print('********************************');
    print('Bem vindo ao jogo da advinhação');
    print('********************************');

    numero_chute = round(random.randrange(1,101));
    total_tentativas = 0;
    rodada = 1;
    pontos = 1000;

    print('Qual nível de dificuldade?');
    print('(1) Fácil | (2) Médio | (3) Difícil');

    nivel = int(input('Define o nível: '));

    if(nivel == 1):
        total_tentativas = 20;
    elif(nivel == 2):
        total_tentativas = 10;
    else:
        total_tentativas = 5;

    for rodada in range(rodada,total_tentativas+1):

        print(f'Tentativa {rodada} de {total_tentativas}');

        chute = int(input('Digite um número entre 1 e 100: '));
        print(f'Voce chutou {chute}');

        if(chute < 1 or chute > 100):
            print('Por favor, digite um número válido! :D');
            continue;


        acertou = numero_chute == chute;
        maior = chute > numero_chute;
        menor = chute < numero_chute;

        if (acertou):
            print(f'Você acertou e fez {pontos} pontos');
            break;
        else:
            if(maior):
                print('Você errou! O seu chute foi maior do que o número secreto :(');
            elif(menor):
                print('Você errou! O seu chute foi menor do que o número secreto :(');
            pontos -= abs(numero_chute - chute);

    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar();