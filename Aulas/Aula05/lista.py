class ContaSalario:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self.codigo == outro.codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"Conta Salário: {self.codigo} Saldo: {self.saldo}"


conta1 = ContaSalario(123)
print(conta1)

conta2 = ContaSalario(123)
print(conta2)


print(conta1 == conta2)

contas = [conta1, conta2]

print(conta1 != conta2)
