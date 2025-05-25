import random

tIn = []
tOut = []
posInicial= []
saida_lab = []
labirinto = []

tentativas = 10000
sucessos = 0

mapa = ["L", "O", "M"]

def gerar_labirinto_aleatorio(lin, col):
    labirinto.clear()
    tIn.clear()
    tOut.clear()

    for i in range(lin):
        linha = []
        for j in range(col):
            linha.append(random.choice(mapa))
        labirinto.append(linha)

    while True:
        for x in range (1, tun + 1):
            (a, b) = ((random.randint(0, lin - 1)),(random.randint(0, col - 1)))
            (c, d) = ((random.randint(0, lin - 1)),(random.randint(0, col - 1)))
            tIn.append((a, b))
            tOut.append((c, d))

        return labirinto, tIn, tOut

def imprimir_labColorido(labirinto):
    vermelho = "\033[91m"
    verde = "\033[92m"
    azul = "\033[94m"
    amarelo = "\033[93m"
    ciano = "\033[96m"
    reset = "\033[0m"

    for linha in labirinto:
        linha_colorida = []
        for c in linha:
            if c == "M":
                linha_colorida.append(f"{ciano}{c}{reset}")
            elif c == "T":
                linha_colorida.append(f"{azul}{c}{reset}")
            elif c == "O":
                linha_colorida.append(f"{vermelho}{c}{reset}")
            elif c == "A":
                linha_colorida.append(f"{verde}{c}{reset}")
            elif c == "S":
                linha_colorida.append(f"{amarelo}{c}{reset}")
            else:
                linha_colorida.append(c)
        print(" ".join(linha_colorida))

print("Escolha uma opção:")
print("1 - Preencher labirinto manualmente")
print("2 - Gerar labirinto aleatório (com Alef e Saída)")
print("3 - Gerar labirinto aleatório (sem Alef nem Saída)")

opcao = input("Opção: ")

if opcao not in ['1', '2', '3']:
    print("Opção inválida. Encerrando a sessão!")
    raise SystemExit

lin = int(input("Informe o numéro de linhas"))

if lin < 1 or lin > 20 :
        print("Valores de linhas e/ou colunas acima do permitido (20). Encerrando o programa!")
        raise SystemExit

col = int(input("Informe o numéro de colunas"))

if col < 1 or col > 20:
    print("Valores de linhas e/ou colunas acima do permitido (20). Encerrando o programa!")
    raise SystemExit

tun = int(input("Informe o numéro de túneis"))

if lin < 1 or lin > 20 or col < 1 or col > 20:
    print("Tamanho inválido! Encerrando.")
    raise SystemExit

if opcao == '2':
    while True:
        labirinto, tIn, tOut = gerar_labirinto_aleatorio(lin, col)
        max_s = int(input("Insira um valor máximo de saídas (máx: 10)"))
        if max_s <= 10:
            saida = random.randint(1, max_s)

            for x in range(1, saida + 1):
                (saida_i, saida_j) = ((random.randint(0, lin - 1)),(random.randint(0, col - 1)))
                labirinto[saida_i][saida_j] = "S"
                saida_lab.append((int(saida_i), int(saida_j)))
            
            i_a = random.randint(0, lin - 1)
            j_a = random.randint(0, col - 1)
            labirinto[i_a][j_a] = "A"
            posInicial.append((i_a, j_a))
            break
        else:
            print("Informe um valor entre 1 e 10!")
            continue

if opcao == '3':
    labirinto, tIn, tOut = gerar_labirinto_aleatorio(lin, col)
    
    PosAlef = input(f"informe o valor da linha e coluna do sapo Alef (separando com espaço)")
    (alef_i, alef_j) = PosAlef.split()
    labirinto[int(alef_i)-1][int(alef_j)-1] = "A"
    posInicial.append((int(alef_i)-1, int(alef_j)-1))
    
    saida = int(input("Informe o numéro de saídas"))

    for x in range(1, saida + 1):
        posSaida = input(f"informe o valor da linha e coluna da saída do labirinto (separando com espaço)")
        (saida_i, saida_j) = posSaida.split()
        labirinto[int(saida_i)-1][int(saida_j)-1] = "S"
        saida_lab.append((int(saida_i)-1, int(saida_j)-1))
    
elif opcao == "1":
    saida = int(input("Informe o numéro de saídas"))

    if lin < 1 or lin > 20 or col < 1 or col > 20:
        print("Valores de linhas e/ou colunas acima do permitido (20). Encerrando o programa!")
        raise SystemExit


    PosAlef = input(f"informe o valor da linha e coluna do sapo Alef (separando com espaço)")
    (alef_i, alef_j) = PosAlef.split()
    posInicial.append((int(alef_i) - 1, int(alef_j) - 1))



    if 0 <= tun <= (lin * col):
        
        for c in range (1, tun + 1):
            enter = input(f"informe o valor da linha e coluna do quadrado do {c}º túnel (separando com espaço)")
            (a, b) = enter.split()
            out = input(f"informe o valor da linha e coluna do quadrado do {c}º túnel (separando com espaço)")
            (c,d) = out.split()
            tIn.append((int(a) - 1, int(b) - 1))
            tOut.append((int(c) - 1, int(d) - 1))

        for x in range(1, saida + 1):
            posSaida = input(f"informe o valor da linha e coluna da saída do labirinto (separando com espaço)")
            (saida_i, saida_j) = posSaida.split()
            saida_lab.append((int(saida_i) - 1, int(saida_j) - 1))

        for i in range(lin):
            linha = []
            for j in range(col):

                if (i, j) in tIn or (i, j) in tOut:
                    linha.append("T")
                    continue
                if (i,j) in posInicial:
                    linha.append("A")
                    continue
                if (i,j) in saida_lab:
                    linha.append("S")
                    continue
                else:
                    while True:
                        entrada = input(f"Elemento da {i + 1}ª linha e {j + 1}ª coluna: ").upper()

                        if entrada in mapa:
                            linha.append(entrada)
                            break
                        else:
                            print(f"Entrada inválida. Use apenas: {mapa}")
                            print("L -> LIVRE")
                            print("O -> OBSTÁCULO")
                            print("M -> MINA")
                            continue
            labirinto.append(linha)
            print("\nLabirinto atualmente")
            imprimir_labColorido(labirinto)

    else:
        print(f"O valor de túneis é inválido! Escolha um valor entre 0 e {lin * col}.")
pos = None
for i in range(lin):
    for j in range(col):
        if labirinto[i][j] == "A":
            pos = (i, j)

if pos is None:
    print("Posição inicial de Alef ('A') não encontrada no labirinto. Encerrando.")
    raise SystemExit
            
#caminhando...
fila = [tuple(pos)]
visitados = [tuple(pos)]
movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]


while fila:
    atual = fila.pop(0)
    i, j = atual

    if labirinto[i][j] == "S":
        print("Caminho encontrado!")
        break

    for mov in movimentos: # mov faz Alef percorrer os caminhos
        novo_j = j + mov[1]
        novo_i = i + mov[0]

        if 0 <= novo_i < lin and 0 <= novo_j < col:
            if labirinto[novo_i][novo_j] not in ("O", "M"):
                if (novo_i, novo_j) not in visitados:
                    fila.append((novo_i, novo_j))
                    visitados.append((novo_i, novo_j))
    destino = None

    if (i, j) in tIn:
        idx = tIn.index((i, j))
        destino = tOut[idx]

    if destino and destino not in visitados:
        fila.append(list(destino))
        visitados.append(destino)

def simular_labirinto(labirinto, tIn, tOut, posInicial, saida_lab, max_passos=1000):
    i, j = posInicial[0]
    
    visitados = set()
    passos = 0
    chance_mina = 2
    minas_encontradas = 0
    while passos < max_passos:
        
        if labirinto[i][j] == "M":
            if random.random() < chance_mina:
                minas_encontradas += 1
                return False #Alef morreu
        else:
            minas_encontradas += 0
        
        visitados.add((i, j))

        if (i, j) in saida_lab:
            return True

        if (i, j) in tIn:
            idx = tIn.index((i, j))
            i, j = tOut[idx]
            continue

        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vizinhos = []
        for mov in movimentos:
            novo_i = i + mov[0]
            novo_j = j + mov[1]

            if 0 <= novo_i < len(labirinto) and 0 <= novo_j < len(labirinto[0]):
                square = labirinto[novo_i][novo_j]
                if square in ("L", "S", "T", "M") and (novo_i, novo_j) not in visitados:
                    vizinhos.append((novo_i, novo_j))

        if not vizinhos:
            return False  # Alef ficou preso

        i, j = random.choice(vizinhos)
        passos += 1

    return False  # Passou do número máximo de passos


for _ in range(tentativas):
    if simular_labirinto(labirinto, tIn, tOut, posInicial, saida_lab, max_passos=1000):
        sucessos += 1

print("\nLabirinto")
imprimir_labColorido(labirinto)
prob = (sucessos / tentativas) * 100
print(f"Probabilidade de Alef chegar até a saída: {prob:.2f}% ({sucessos}/{tentativas})")

while True:
    repetir = input("\nDeseja refazer a simulação com o mesmo labirinto? (s/n): ").lower()
    if repetir == 's':
        sucessos = 0
        for _ in range(tentativas):
            if simular_labirinto(labirinto, tIn, tOut, posInicial, saida_lab, max_passos=1000):
                sucessos += 1
        
        prob = (sucessos / tentativas) * 100
        print(f"Probabilidade de Alef chegar até a saída: {prob:.2f}% ({sucessos}/{tentativas})")

        print("\nLabirinto")
        imprimir_labColorido(labirinto)

    elif repetir == "n":
        print("Sessão encerrada, até a próxima!")
        raise SystemExit
    else:
        print("Digite 's' para sim ou 'n' para não.")