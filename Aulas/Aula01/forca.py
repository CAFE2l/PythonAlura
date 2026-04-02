
cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

fundo = {
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}
def jogo_forca():
    converte = "Bem vindo ao jogo da forca"

    print(f"{estilos['negrito']}{cores['azul']}{'==='*5+'=='}{cores['cinza']}EXTENSO{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['verde']}{'==='*5}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}{cores['cinza']}{converte.center(39)}{estilos['reset']}")
    print(f"{cores['vermelho']}{estilos['negrito']}{'==='*13}{estilos['reset']}")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False 
    #enquanto (True)
    while(not enforcou and not acertou):

        chute = input("Qual a leta? ")
        chute = chute.strip()
        index = 0 

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"{estilos['negrito']}{cores['cinza']}Encontrei a letra {cores['azul']}{letra}{cores['cinza']} na posição {cores['vermelho']}{index}{cores['cinza']}")
            index += 1;

        print("jogando...")




if(__name__ == "__main__"):
    jogo_forca()

