def contagem_regressiva():
    minutos = 10
    segundos = 0
    while minutos >= 0:
        print(f"{minutos:02d}:{segundos:02d}")
        if segundos == 0:
            minutos -= 1
            segundos = 59
        else:
            segundos -= 1
        if minutos == 8 and segundos == 57:  # para não imprimir infinitamente
            break

contagem_regressiva()
