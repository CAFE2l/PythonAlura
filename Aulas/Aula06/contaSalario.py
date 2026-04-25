from functools import total_ordering
from operator import attrgetter


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __eq__(self, other):
        if type(other) != ContaSalario:  # noqa: E721
            return False

        return self.codigo == other.codigo and self.saldo == other.saldo

    def __lt__(self, other):
        if self.saldo != other.saldo:
            return self.saldo < other.saldo
        return self.codigo < other.codigo

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Conta Salário - Código: {self.codigo}, Saldo: {self.saldo}"


conta_do_joao = ContaSalario(1023)
conta_do_joao.deposita(100)
# print(conta_do_joao)

conta_da_maria = ContaSalario(123)
conta_da_maria.deposita(1000)
# print(conta_da_maria)

conta_do_paulo = ContaSalario(456)
conta_do_paulo.deposita(100)
# print(conta_do_paulo)

contas = [conta_do_joao, conta_da_maria, conta_do_paulo]


def extrai_saldo(conta):
    return conta.saldo


for conta in sorted(contas, key=attrgetter("saldo", "codigo")):
    print(conta)


print(conta_do_joao <= conta_do_joao)
