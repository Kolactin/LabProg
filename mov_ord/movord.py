def insertion_sort_desv(arr):
    deslocamentos = 0
    for i in range(1, len(arr)):
        atual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > atual:
            arr[j + 1] = arr[j]  # Desloca para a direita
            deslocamentos += 1
            j -= 1
        arr[j + 1] = atual
    return deslocamentos

def main():
    t = int(input("Número de casos de teste: "))
    for _ in range(t):
        n = int(input("Tamanho do vetor: "))
        vetor = list(map(int, input("Vetor: ").split()))
        resultado = insertion_sort_desv(vetor)
        print("Deslocamentos realizados:", resultado)

if __name__ == '__main__':
    main()