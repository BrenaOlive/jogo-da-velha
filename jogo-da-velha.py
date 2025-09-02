# Jogo da Velha
# AD1 - FUNDAMENTOS DE PROGRAMAÇÃO - Brena Alves
# Matricula: 25113050400 - Polo: Belford Roxo

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tab):
    print("\n")
    for i in range(3):
        linha = ""
        for j in range(3):
            linha += f"_{tab[i][j]}_" if tab[i][j] != " " else "___"
            if j < 2:
                linha += "|"
        print(linha)
    print()

def verificar_vencedor(tab):
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != " ":
            return tab[i][0]
        if tab[0][i] == tab[1][i] == tab[2][i] != " ":
            return tab[0][i]
    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        return tab[0][0]
    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return tab[0][2]
    if all(tab[i][j] != " " for i in range(3) for j in range(3)):
        return "Empate"
    return None

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador = "X"
    while True:
        mostrar_tabuleiro(tabuleiro)
        try:
            pos = int(input(f"Jogador {jogador}, escolha uma posição de 1 a 9: "))
        except ValueError:
            print("Entrada inválida, digite um número!")
            continue

        if pos < 1 or pos > 9:
            print("Digite um número de 1 a 9!")
            continue

        linha = (pos - 1) // 3
        coluna = (pos - 1) % 3

        if tabuleiro[linha][coluna] != " ":
            print("Posição ocupada, tente novamente!")
            continue

        tabuleiro[linha][coluna] = jogador
        resultado = verificar_vencedor(tabuleiro)
        if resultado:
            mostrar_tabuleiro(tabuleiro)
            if resultado == "Empate":
                print("Empate! Ninguém venceu.")
            else:
                print(f"Vitória do jogador {resultado}!")
            return resultado

        jogador = "O" if jogador == "X" else "X"

def main():
    placar = {"X": 0, "O": 0, "Empate": 0, "Partidas": 0}
    while True:
        resultado = jogar()
        placar["Partidas"] += 1
        placar[resultado] += 1
        print("\nPLACAR:")
        print(f"Partidas: {placar['Partidas']}")
        print(f"Vitórias X: {placar['X']}")
        print(f"Vitórias O: {placar['O']}")
        print(f"Número de Empates: {placar['Empate']}")

        cont = input("Deseja jogar novamente? (s/n): ").lower()
        if cont != "s":
            break
    print("Obrigado por jogar!")

if __name__ == "__main__":
    main()