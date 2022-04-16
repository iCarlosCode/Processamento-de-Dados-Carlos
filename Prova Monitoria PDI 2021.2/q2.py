import numpy as np

def main():
    # Pede pra o usuário decidir o tamanho
    n = int(input('Diga o tamanho da matriz nxn: '))
    # Gera a matriz
    matriz = np.random.randint(10,size=(n,n))
    print('A matriz gerada é:')
    print(matriz)

    # Realiza as trocas
    matriz = trocarColunas(matriz)
    matriz = trocarLinhas(matriz)
    print(f'A matriz final é:')
    print(matriz)

# Troca linhas
def trocarLinhas(matriz):
    for i in range(0, len(matriz)-1, 2):
        aux = matriz[i+1].copy()
        matriz[i+1] = matriz[i].copy()
        matriz[i] = aux.copy()

    return matriz

# Troca Colunas
def trocarColunas(matriz):
    for l in matriz:
        for i in range(0, len(l)-1, 2):
            l[i], l[i+1] = l[i+1], l[i]
    return matriz

main()