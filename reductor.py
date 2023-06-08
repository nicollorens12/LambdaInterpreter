from arbre import *

def reduce(a: Arbre) -> Arbre:
    match a:
        case Buit():
            return Buit()
        case Node(x,Buit(),Buit()):
            print("paso por Node")
            return x 
        case Node("\\",e,d):
            return "(\\" + arbre2String(e) + "." + arbre2String(d) +")"
        case Node("λ",e,d):
            print("paso por lam")
            return "(λ" + arbre2String(e) + "." + arbre2String(d) +")"
        case Node(x,e,d):
            print("paso por ultimo")
            print(x.getText())
            return "(" + x + arbre2String(e) + arbre2String(d) +")"
        case _:
            print("estamos aqui")