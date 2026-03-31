import random
from time import sleep

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

def jogo_adivinha():
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000  # Initialize pontos (points)

    print(f"{estilos['negrito']}{cores['azul']}{'==='*5+'=='}{cores['cinza']}EXTENSO{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['verde']}{'==='*5}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}{cores['cinza']}{'Bem vindo ao jogo de Adivinhação'.center(39)}{estilos['reset']}")
    print(f"{cores['vermelho']}{estilos['negrito']}{'==='*13}{estilos['reset']}")
    
    print(f"{cores['cinza']}{estilos['negrito']}Qual nível de dificuldade?")
    print(f"{cores['verde']}(1) {cores['cinza']}Fácil {cores['amarelo']}(2){cores['cinza']} Médio {cores['vermelho']}(3) {cores['cinza']}Difícil")

    nivel = int(input(f"Escolha um nível: "))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2): 
        total_de_tentativas = 7
    else:
        total_de_tentativas = 3

    # Fixed indentation - now the for loop is at the correct level
    for rodada in range(1, total_de_tentativas + 1):
        print(f"{estilos['negrito']}{cores['cinza']}Tentativa {cores['vermelho']}{rodada}{cores['cinza']} de{cores['vermelho']} {total_de_tentativas}")
        
        chute = int(input(f"{cores['cinza']}Digite um número entre 1 e 100: "))
        print(f"voce digitou {cores['roxo']}{chute}")
        
        if(chute < 1 or chute > 100):
            print(f"{cores['vermelho']}voce deve digitar um numero entre 1 e 100")
            continue
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"{cores['verde']}{estilos['italico']}Parabéns! Você acertou e fez {pontos} pontos{cores['limpa']}")
            break
        else:
            if(maior):
                print(f"{estilos['negrito']}O seu chute foi maior do que o número secreto!")
            elif(menor):
                print(f"{estilos['negrito']}O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"{cores['vermelho']}Fim do jogo{cores['limpa']}")

    if(__name__ == "__main__"):
        jogo_adivinha()

