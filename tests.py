from listas import List

if __name__ == '__main__':
    lista = List(2,3,4,5)
    lista.print(sep=' > ')

    lista.append_start([1,6,7])
    lista.print()

    lista.append_end([10,11,12])
    lista.print()

    lista.append_pos([8,17], 2)
    lista.print()

    print(lista.get_pos(1))
    print(lista.get_pos(5))