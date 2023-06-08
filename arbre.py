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

def equal(arbol1: Arbre, arbol2: Arbre) -> bool:
    if isinstance(arbol1, Buit) and isinstance(arbol2, Buit):
        return True
    elif isinstance(arbol1, Node) and isinstance(arbol2, Node):
        return (
            arbol1.val == arbol2.val and
            equal(arbol1.esq, arbol2.esq) and
            equal(arbol1.dre, arbol2.dre)
        )
    else:
        return False


def arbre2String(a: Arbre) -> string:
   match a:
        case Buit():
            return ""
        case Node(x,Buit(),Buit()):
            return x 
        case Node("\\",e,d):
            return "(\\" + arbre2String(e) + "." + arbre2String(d) +")"
        case Node("λ",e,d):
            return "(λ" + arbre2String(e) + "." + arbre2String(d) +")"
        case Node(x,e,d):
            return "(" + x + arbre2String(e) + arbre2String(d) +")"
