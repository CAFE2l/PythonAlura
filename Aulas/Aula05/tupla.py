conta_do_gui = (15, 1000)


def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)


print(deposita(conta_do_gui))
print(conta_do_gui)

conta_do_gui = deposita(conta_do_gui)
