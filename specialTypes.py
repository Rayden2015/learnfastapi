from typing import List, Tuple, Dict
# following line declares a List object of strings.
# If violated, mypy shows error
cities: List[str] = ['Mumbai', 'Delhi', 'Chennai']
# This is Tuple with three elements respectively
# of str, int and float type)
employee: Tuple[str, int, float] = ('Ravi', 25, 35000)
# Similarly in the following Dict, the object key should be str
# and value should be of int type, failing which
# static type checker throws error
marklist: Dict[str, int] = {'Ravi': 61, 'Anil': 72}

def sayhello(name: str):
     a =  "Hello " + " " + name.swapcase()
     print(a)

sayhello("nurudin")


class rectangle:
    def __init__(self, w:int, h:int) -> None:
        self.width = w
        self.height = h

def area(r:rectangle) -> int:
        return r.width * r.height

r1=rectangle(10,20)
print("area = ", area(r1))