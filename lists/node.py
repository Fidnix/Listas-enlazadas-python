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
