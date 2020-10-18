'''
class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo;
        self.saldo  = 0;

    def depositar(self, valor):
        self.saldo += valor;

    def __str__(self):
        return f'>>[Codigo {self.codigo} Saldo {self.saldo}]<<';

contaIsaque = ContaCorrente(18);
contaIsaque.depositar(320);

contaRose = ContaCorrente(20);
contaRose.depositar(1000);
'''
from abc import ABCMeta, abstractmethod;

class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo;
        self._saldo = 0;

    def depositar(self, valor):
        self._saldo += valor;

    @abstractmethod
    def passaOMes(self):
        pass;

    def __str__(self):
        return f'>>[Codigo {self._codigo} Saldo {self._saldo}]<<'

class ContaCorrente(Conta):
    def passaOMes(self):
        self._saldo -= 2;

class ContaPoupanca(Conta):
    def passaOMes(self):
        self._saldo *= 1.01;
        self._saldo -= 3;
'''
contaIsaque = ContaCorrente(18);
contaIsaque.depositar(1000)
contaIsaque.passaOMes();
print(contaIsaque);

contaPoupancaIsaque = ContaPoupanca(19);
contaPoupancaIsaque.depositar(1000);
contaPoupancaIsaque.passaOMes();
print(contaPoupancaIsaque);
'''

contaIsaque = ContaCorrente(18);
contaIsaque.depositar(1000);

contaPoupancaIsaque = ContaPoupanca(17);
contaPoupancaIsaque.depositar(1000);

contas = [contaIsaque, contaPoupancaIsaque];

for conta in contas:
    conta.passaOMes();
    print(conta);

from functools import total_ordering;

@total_ordering
class ContaSalario():
    def __init__(self, codigo):
        self._codigo = codigo;
        self._saldo = 0;

    def __eq__(self, outro):
        if not isinstance(outro, ContaSalario):
            return False;
        return self._codigo == outro._codigo;

    def __lt__(self, outro):
        return self._saldo < outro._saldo;

    def depositar(self, valor):
        self._saldo += valor;

    def __str__(self):
        return f'>>[Codigo {self._codigo} Saldo {self._saldo}]<<';

contaSalario1 = ContaSalario(17);
contaSalario1.depositar(500);
contaSalario2 = ContaSalario(17);
contaSalario3 = ContaPoupanca(17);
contaSalario3.depositar(1000);

print(contaSalario1  > contaSalario3);
