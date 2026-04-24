class Conta:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"Conta {self.codigo} Saldo: {self.saldo}"


print(Conta(88))


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(1000)
conta_do_gui.passa_o_mes()
print(conta_do_gui)


conta_da_dani = ContaPoupanca(17)
conta_da_dani.deposita(1000)
conta_da_dani.passa_o_mes()
print(conta_da_dani)
contas = [conta_do_gui, conta_da_dani]

for conta in contas:
    conta.passa_o_mes()
    print(conta)
