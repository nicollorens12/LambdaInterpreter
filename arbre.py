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

def equal(tree1: Arbre, tree2: Arbre) -> bool:
    if isinstance(tree1, Buit) and isinstance(tree2, Buit):
        return True
    elif isinstance(tree1, Node) and isinstance(tree2, Node):
        return ( tree1.val == tree2.val and equal(tree1.esq, tree2.esq) and equal(tree1.dre, tree2.dre))
    else:
        return False


def abre2String(a: Arbre) -> string:

    match a:
        case Buit():
            return ""
        case Node(x,Buit(),Buit()):
            return x 
        
        case Node("\\",e,d):
            return "(\\" + abre2String(e) + "." + abre2String(d) +")"
        
        case Node("λ",e,d):
            return "(λ" + abre2String(e) + "." + abre2String(d) +")"
        
        case Node(x,e,d):
            return "(" + x + abre2String(e) + abre2String(d) +")"