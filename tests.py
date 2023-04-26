from lists import *

if __name__ == '__main__':
    lista = List(2,3,4,5)
    print("Se creo la lista1: ")
    lista.print(sep=' > ')
    lista.table()
    print("\n")

    print("Se agregaron los elementos al inicio de la lista1: ")
    lista.append_start([1,6,7])
    lista.print()
    print("\n")

    print("Se agregaron los elementos al final de la lista1: ")
    lista.append_end([10,11,12])
    lista.print()
    print("\n")

    print("Se agregaron los elementos en la posicion 2: ")
    lista.append_pos([8,17], 2)
    lista.print()
    print("\n")

    print("Obtencion del elemento en posicion 1 de lista1: ")
    print(lista.get_pos(1))
    print("Obtencion del elemento en posicion 5 de lista1: ")
    print(lista.get_pos(5))
    print("")

    print("Obtencion del elemento 23 de una lista vacia: ")
    try:
        lista_vacia = List()
        print(lista_vacia.get_pos(23))
    except:
        print("Hubo un error...")
    print("")

    print("Poner el elemento 100 en la posicion 5 de lista1")
    lista.set_pos(elem=100, n= 5)
    lista.print()
    print("")

    print("Eliminar y obtener el primer elemento de la lista:")
    print( lista.pop_start() )
    lista.print()
    print("")

    print("Eliminar y obtener el ultimo elemento de la lista:")
    print( lista.pop_end() )
    lista.print()
    print("")

    print("Eliminar y obtener el sexto elemento de la lista:")
    print( lista.pop_pos(6) )
    lista.print()
    print("")