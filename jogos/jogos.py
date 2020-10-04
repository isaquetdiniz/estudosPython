import advinhacao;
import forca;

def escolha():

    print('*********************************');
    print('*******Escolha o seu jogo!*******');
    print('*********************************');

    print('(1) Forca | (2) Advinhação');
    jogo = int(input('Digite o número: '));

    if(jogo == 1):
        print('Jogando Forca');
        forca.jogar();
    elif(jogo == 2):
        print('Jogar Advinhação');
        advinhacao.jogar();

if(__name__ == '__main__'):
    escolha();
