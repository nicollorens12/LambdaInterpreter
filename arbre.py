from __future__ import annotations
from dataclasses import dataclass
import string

class Buit:
    pass

@dataclass
class Node:
    val: string
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

def mida(a: Arbre) -> int:
    match a:
        case Buit():
            return 0
        case Node(x, e, d):
            return 1 + mida(e) + mida(d)

t = Node(1,Node(2,Buit(),Buit()),Node(3,Buit(),Buit()))

print('mida:', mida(t))