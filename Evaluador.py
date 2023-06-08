from arbre import *

class funcionsEvaluador:
    
    def reduccionBeta(self,arbol: Arbre) -> Arbre:
        match arbol:
            case Buit():
                return Buit
            case Node("",Node("\\",a,b),d):
                return self.subtitucion(a,b,d)
            case Node("",Node("λ",a,b),d):
                return self.subtitucion(a,b,d)
            #case Node(x,i,d):
            #    new_i = self.reduceBeta(i)
            #    new_d = self.reduceBeta(d)
            #    return Node(x,new_i,new_d)
            case _:
                return arbol
    
    def subtitucion(self, arbol: Arbre, var: Arbre, argud: Arbre) -> Arbre:
        match var:
            case Node(x, Buit(),Buit()):
                if arbol.val == x:
                    return argud
                else:
                    return var
            case Node(x,i,d):
                new_i = self.subtitucion(arbol,i,argud)
                new_d = self.subtitucion(arbol,d,argud)
                return Node(x,new_i,new_d)
            case _:
                return arbol
    
    #Funcion que comprueba si tiene que substituir las variables del lamda para no crear inconsistencias.
    def comprovarConversion(self, arbol: Arbre) -> Arbre:
        match arbol:
            case Node("",Node("λ",a,b,e),d):
                return Buit()
            case Node("",Node("\\",a,b,e),d):
                return Buit()
            case _:
                return arbol
                
    def reducirExp(self, a: Arbre, max_reductions: int) -> Arbre:
        reduced = self.reduccionBeta(a)
        if(not equal(a,reduced)): 
            print("β-reducció:")
            print(arbre2String(a) + " -> " + arbre2String(reduced))
        
        return reduced

    def evaluarExp(self, arbol: Arbre, maxIt: int = 100):
        already_reduced = False
        i = 1
        repe = 0
        while(i <= maxIt):
            reduced = self.reduccionBeta(arbol) #FALTA AFEGIR a reducirExp el match comentado de abajo para identifcar los casos en los que la reduccion no esta a la izquierda del todo
            #print("Esta es la reduccion " + arbre2String(reduced))
            if not equal(arbol,reduced):
                #print("HOLA")
                already_reduced = True
                repe = 0
                print("β-reducció:")
                print(arbre2String(arbol) + " -> " + arbre2String(reduced))
                #print("DESDE EL PRIMER IF")
                
                match reduced:
                    case Node("",Node(x,Buit(),Buit()),d):
                        #print("primer caso")
                        reduced = Node('',Node(x,Buit(),Buit()),self.reducirExp(d,maxIt))
                    case Node("",x,d):
                        #print("segundo caso")
                        reduced = Node('',self.reducirExp(x,maxIt),self.reducirExp(d,maxIt))
                arbol = reduced
                
            elif equal(arbol,reduced) and repe < 3 and not already_reduced: # Es irreducible desde el principio
                repe += 1
                #print("Cas elif")
                print("β-reducció:")
                print(f"{arbre2String(arbol)} -> {arbre2String(reduced)}")
                arbol = reduced
            elif equal(arbol,reduced) and already_reduced: #puede ser igual porque ha llegado a forma normal o porque es irreducible desde el principio
                i = maxIt + 1
            elif equal(arbol,reduced) and repe == 3:
                i = maxIt + 1
                repe += 1
                print("...")
                reduced = arbol
            else :
                break
            
                    
            
            i += 1
        print("Resultat: ")
        if already_reduced:
            
            print(f"{arbre2String(reduced)}")
        else:
            print("Nothing")
