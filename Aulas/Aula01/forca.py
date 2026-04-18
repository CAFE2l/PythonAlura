import random
from pathlib import Path  # Adicionado para localizar arquivo corretamente

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
def imprime_mensagem_aberutra():
    converte = "Bem vindo ao jogo da forca"   
    print(f"{estilos['negrito']}{cores['azul']}{'==='*5+'=='}{cores['cinza']}EXTENSO{cores['limpa']}{cores['cinza']}{estilos['negrito']}{cores['verde']}{'==='*5}{estilos['reset']}")
    print(f"{cores['cinza']}{estilos['negrito']}{cores['cinza']}{converte.center(39)}{estilos['reset']}")
    print(f"{cores['vermelho']}{estilos['negrito']}{'==='*13}{estilos['reset']}")
    
def jogo_forca():

    imprime_mensagem_aberutra()
    # Carrega as palavras do arquivo (usando pathlib para garantir o caminho correto)
    try:
        # Garante que o arquivo seja buscado no mesmo diretório do script
        caminho_arquivo = Path(__file__).parent / "palavras.txt"
        arquivo = open(caminho_arquivo, "r", encoding="utf-8")
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            if linha:  # Ignora linhas vazias
                palavras.append(linha)
        arquivo.close()
        
        # Verifica se o arquivo tem palavras
        if not palavras:
            print(f"{cores['vermelho']}Erro: Arquivo palavras.txt está vazio!{cores['limpa']}")
            return
            
    except FileNotFoundError:
        print(f"{cores['vermelho']}Erro: Arquivo palavras.txt não encontrado!{cores['limpa']}")
        print(f"Procurei em: {caminho_arquivo}")
        print("Crie um arquivo palavras.txt com uma palavra por linha.")
        return
    
    # Sorteia uma palavra aleatória
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    
    # Cria a lista de letras acertadas
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False 
    erros = 0

    print(f"\nPalavra com {len(palavra_secreta)} letras: {' '.join(letras_acertadas)}\n")
    
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip().lower()
        
        # Valida se o usuário digitou uma letra
        if len(chute) != 1 or not chute.isalpha():
            print(f"{cores['amarelo']}Digite apenas uma letra!{cores['limpa']}")
            continue
        
        # Verifica se o chute já foi descoberto
        if chute in letras_acertadas:
            print(f"{cores['amarelo']}Você já acertou essa letra!{cores['limpa']}")
            continue
            
        # Verifica se o chute está na palavra
        if chute in palavra_secreta:
            print(f"{estilos['negrito']}{cores['cinza']}Encontrei a letra {cores['azul']}{chute}{cores['cinza']} na(s) posição(ões):", end=" ")
            
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
                    print(f"{cores['vermelho']}{index}{cores['cinza']}", end=" ")
            print()
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
  

    def imprime_mensagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        # Fim do jogo
    def imprime_mensagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    if acertou:
        imprime_mensagem_vencedor() 
    else:
        imprime_mensagem_perdedor()
    print(f"{cores['vermelho']}{estilos['negrito']}fim de jogo{cores['limpa']}")

if __name__ == "__main__":
    jogo_forca()
