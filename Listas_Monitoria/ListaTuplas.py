'''
Lista de tuplas da monitoria de Programação I
'''

def question1():
    times = 0;
    tupla = (11,21,31,[33,52],44,[33,52],55);

    for i in range(0, len(tupla)):
        if isinstance(tupla[i], list) and 52 in tupla[i] and times <= 0:
            position = tupla[i].index(52);
            tupla[i][position] = 555;
            print(tupla);
            times += 1;
##question1();

def question2():
    times = 0;
    tupla = (50, 10, 60, 70, 50, 43, 23, 78, 101, 50, 23);

    for i in range(0, len(tupla)):
        if tupla[i] == 50:
            times += 1;

    print(f'{times} vezes');

##question2();

def question3():
    tupla = (1, 2, 3,'a','b', 6, 7, 'c');
    palavra = [];

    for i in range(0, len(tupla)):
        if isinstance(tupla[i], str):
            palavra.append(tupla[i]);

    print(palavra);

##question3();

def question4():
    dict1 = {'Dez': 10, 'Vinte': 20, 'Trinta': 30};
    dict2 = {'Trinta': 30, 'Quarenta': 40, 'Cinquenta': 50};

#    for key in dict2:
#       dict1[key] = dict2[key];

    dict1.update(dict2);
    print(dict1);

##question4();

def question5():
    test_list = [];
    test_dict2 = {'python': 4, 'is': 10, 'best': 11};
    sub_list2 = [4, 10, 11];

    test_dict = {'python': 4, 'chave1': 10, 'chave2': 11};
    sub_list = [4, 11, 10];

    for i in test_dict:
        test_list.append(test_dict[i])

    print(sub_list == test_list);

question5();


