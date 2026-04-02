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

    palavra_secreta = "uva"
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False 
    erros = 0

    print(letras_acertadas)
    
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().lower()  # Converte para minúsculo
        
        # Verifica se o chute já foi descoberto
        if chute in letras_acertadas:
            print(f"{cores['amarelo']}Você já acertou essa letra!{cores['limpa']}")
            continue
            
        # Verifica se o chute está na palavra
        if chute in palavra_secreta:
            print(f"{estilos['negrito']}{cores['cinza']}Encontrei a letra {cores['azul']}{chute}{cores['cinza']} na(s) posição(ões):", end=" ")
            
            encontrou = False
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
                    print(f"{cores['vermelho']}{index}{cores['cinza']}", end=" ")
                    encontrou = True
            print()  # Pula linha após mostrar as posições
        else:
            erros += 1
            print(f"{cores['vermelho']}Letra '{chute}' não encontrada! Erros: {erros}/6{cores['limpa']}")
        
        # Verifica se enforcou
        enforcou = erros == 6
        
        # Verifica se acertou todas as letras
        acertou = "_" not in letras_acertadas
        
        # Mostra o progresso atual
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Erros restantes: {6 - erros}\n")
    
    # Fim do jogo
    if acertou:
        print(f"{cores['verde']}{estilos['negrito']}Parabéns! Você ganhou! A palavra era {palavra_secreta}{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}{estilos['negrito']}Você foi enforcado! A palavra era {palavra_secreta}{cores['limpa']}")
    
    print(f"{cores['vermelho']}{estilos['negrito']}fim de jogo{cores['limpa']}")

if __name__ == "__main__":
    jogo_forca()
