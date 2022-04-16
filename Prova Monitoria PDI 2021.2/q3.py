# Algoritimo para colocar a lista v em ordem do menor para o maior

v = [54,26,93,17,77,31,44,55,20]
# Cria-se um loop infinito com While True
trocou = True
while trocou:
    # Desativa-se o While True
    trocou = False

    # Ocorre a iteração por cada elemento da lista v, checando se o sucessor é maior do que o antecessor até que não ocorra nenhuma troca e o trocou vira False e sai do While Loop
    # É importante fazer len(v)-1 porque a lista começa da posição 0 e vai até len(v)-1
    for i in range (len(v)-1):
        # Checa se o valor atual é maior do que o valor do sucessor
        if v[i] > v[i+1]:
            # Quando é maior o While True é setado para continurar com o algoritimo de sorteio
            trocou = True

            # Ocorre a troca de posicão para que o maior seja o sucessor
            aux = v[i]
            v[i] = v[i+1]
            v[i+1] = aux
