from typing import Union
from lists.node import Node

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
        for _ in range(0, self._size-1):
            output += f'{current_node._elem}{sep}'
            current_node = current_node._sig
        output+=f'{current_node._elem}'
        print(output)

    def empty_list(self) -> bool:
        return self._size == 0
    
    def get_size(self) -> int:
        return self._size
    
    def verify_get_pos(function):
        def func(self, n: int = 1):
            if(n<=0 or n >self._size):
                raise Exception("Error: 'n' esta fuera de rango")
            if(self.empty_list()):
                return
            return function(self, n=n)
        return func

    
    def verify_set_pos(function):
        def func(self, elem: int = None, n: int = 1):
            if(n<=0 or n >self._size):
                raise Exception("Error: 'n' esta fuera de rango")
            if( elem==None ):
                raise Exception("Error: El valor de n no puede ser None")
            if(self.empty_list()):
                return
            return function(self, elem=elem, n=n)
        return func
    
    @verify_get_pos
    def get_pos(self, n: int = 1) -> int:
        current_node = self._head
        for _ in range(1, n):
            current_node = current_node._sig
        return current_node._elem

    @verify_set_pos
    def set_pos(self, elem: int = None, n: int = 1) -> None:
        current_node = self._head
        for _ in range(1, n):
            current_node = current_node._sig
        current_node._elem = elem

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
        if(n <= 0 or n > self._size):
            raise Exception("Error: 'n' esta fuera de rango")
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

    def pop_start(self) -> int:
        if(self.empty_list()):
            return
        initial_value = self._head._elem
        self._head = self._head._sig
        self._size -= 1
        return initial_value

    def pop_end(self) -> int:
        if(self.empty_list()):
            return
        current_node = self._head
        for _ in range(2, self._size):
            current_node = current_node._sig
        final_value = current_node._sig._elem
        current_node._sig = None
        self._size -= 1
        return final_value
    
    def pop_pos(self, n: int = 1) -> int:
        if(self.empty_list()):
            return
        if(n <= 0 or n > self._size):
            raise Exception("Error: 'n' esta fuera de rango")
        current_node = self._head
        for _ in range(2, n):
            current_node = current_node._sig
        n_value = current_node._sig._elem
        prev_node = current_node._sig._sig
        current_node._sig = prev_node
        self._size -= 1
        return n_value

    def table(self):
        max_space: int = 1
        power: int = 10
        while(self._size >= power):
            max_space += 1
            power *= 10
        
        hr =f"{'_'*(8+(self._size+1)*max_space)}"
        row1 = '|pos  |'
        row2 = '|value|'
        current_node = self._head
        for i in range(1, self._size):
            row1+=f'{i: <{max_space}}|'
            row2+=f'{current_node._elem: <{max_space}}|'
            current_node=current_node._sig
        print(f"{hr}\n{row1}\n{hr}\n{row2}\n{hr}")