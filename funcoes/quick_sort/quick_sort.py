def quick_sort(produtos):
    if len(produtos) < 2:
        return produtos
    else:
        pivo = produtos[0]
        menores = [i for i in produtos[1:] if i.id < pivo.id]
        maiores = [i for i in produtos[1:] if i.id >= pivo.id]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)
