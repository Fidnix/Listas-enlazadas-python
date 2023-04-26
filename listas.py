from typing import Union

class Node:
    _elem: int
    _sig: 'Node'

    def __init__(
            self,
            elems: Union[int, list[int]] = 0
    ) -> None:
        if(type(elems) == int):
            self._sig = None
            self._elem = elems
            return
        current_node = self
        current_node._elem = elems[0]
        for i in range(1, len(elems)):
            print(f'{elems[i]}: {type(elems[i])}')
            current_node._sig = Node( elems[i] )
            current_node = current_node._sig

    def add(
            self,
            elem: Union[int, 'Node'] = 0
    ) -> None:
        current_node = self
        while(current_node._sig != None):
            current_node = current_node._sig
        if(type(elem) == int):
            current_node._sig = Node(elem)
        else:
            current_node._sig = elem

    def print(self) -> None:
        output = f'{self._elem} '
        current_node = self._sig
        while(current_node != None):
            output += f'{current_node._elem} '
            current_node = current_node._sig
        print(output)

class List:
    _size: int
    _head: Node

    def __init__(
            self,
            *elems: int 
        ) -> None:
        if(len(elems) == 0):
            self._size = 0
            self._head = None
            return
        self._size = len(elems)
        self._head = Node(elems)

    def print(self, sep: str = ' '):
        output = ''
        current_node = self._head
        for _ in range(0, self._size):
            output += f'{current_node._elem}{sep}'
            current_node = current_node._sig
        print(output)

    def void_list(self) -> bool:
        return self._size == 0
    
    def get_size(self) -> int:
        return self._size
    
    def get_pos(self, n: int = 0) -> int:
        if(n<=0 or n > self._size):
            raise Exception('Error: la posición de una lista no puede ser negativa o mayor a la longitud de la lista')
        if(self.void_list()):
            return
        current_node = self._head
        for _ in range(1, n):
            current_node = current_node._sig
        return current_node._elem

    def append_start(self, elems: Union[int, list[int]] = 0) -> None:
        new_node = Node(elems)
        new_node.add(self._head)
        self._head = new_node
        if(type(elems)==int):
            self._size += 1
            return
        self._size += len(elems)

    def append_end(self, elems: Union[int, list[int]] = 0) -> None:
        current_node = self._head
        for _ in range(1, self._size):
            current_node = current_node._sig
        new_node = Node(elems)
        current_node._sig = new_node
        if(type(elems)==int):
            self._size += 1
            return
        self._size += len(elems)

    def append_pos(self, elems: Union[int, list[int]] = 0, n: int = 1) -> None:
        if(n <= 0):
            raise Exception('Error: la posición de una lista no puede ser negativa')
        current_node = self._head
        for _ in range(2, n):
            current_node = current_node._sig
        next_nodes = current_node._sig
        new_node = Node(elems)
        new_node.add(next_nodes)
        current_node._sig = new_node
        if(type(elems)==int):
            self._size += 1
            return
        self._size += len(elems)

    def pop_start(self):
        pass

    def pop_end(self):
        pass
    
    def pop_pos(self, n: int = 0) -> None:
        pass