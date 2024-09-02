def invertePalavra(palavra):
    PalavraInicial = palavra
    PalavraInvertida = []

    i = len(PalavraInicial)

    while i > 0:
        PalavraInvertida += PalavraInicial[i-1]
        i -= 1
    for item in PalavraInvertida:
        print(item, end=' ')


invertePalavra("inverteu")
