def Conta(titular, saldo):
    def deposita(valor):
        nonlocal saldo
        saldo += valor

    def extrato():
        return f"Titular: {titular}, Saldo: {saldo}"

    return {"deposita": deposita, "extrato": extrato}


conta_do_gui = Conta("Gui", 1000)
conta_da_dani = Conta("Dani", 500)


def deposita_para_todas(contas):
    for conta in contas:
        conta["deposita"](100)


contas = [conta_do_gui, conta_da_dani]
deposita_para_todas(contas)
# print(conta_do_gui["extrato"]())
# print(conta_da_dani["extrato"]())
usuarios = [conta_da_dani, conta_do_gui]
usuarios.append(Conta("Paulo", 2000))


conta_do_gui["deposita"](500)
conta_da_dani["deposita"](200)

contas = [conta_do_gui, conta_da_dani]

print(contas)
for conta in contas:
    print(conta["extrato"]())
