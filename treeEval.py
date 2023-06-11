from arbre import *

class functionsArbre:
    
    lambda1 = "λ"
    lambda2 = "\\"
    
    respuesta_evaluada = []
    

    def reduceBeta(self,arbol: Arbre) -> Arbre:
        match arbol:
            case Buit():
                return Buit
            case Node("",Node("\\",a,b),d):
                return self.substitucion(a,b,d)
            case Node("",Node("λ",a,b),d):
                return self.substitucion(a,b,d)
            case _:
                return arbol
    
    def substitucion(self, arbol: Arbre, var: Arbre, argud: Arbre) -> Arbre:
        match var:
            case Node(x, Buit(),Buit()):
                if arbol.val == x:
                    return argud
                else:
                    return var
            case Node(x,i,d):
                new_i = self.substitucion(arbol,i,argud)
                new_d = self.substitucion(arbol,d,argud)
                return Node(x,new_i,new_d)
            case _:
                return arbol

    def reduce(self, arbol: Arbre) -> Arbre:
        if arbol != None and arbol != Buit():
            reduced = self.reduceBeta(arbol)
            if not equal(reduced,arbol):
                #print("β-reducción:")
                self.respuesta_evaluada.append((abre2String(arbol) + " -> β-> " + abre2String(reduced),reduced))
                #print(f"{abre2String(arbol)} -> {abre2String(reduced)}")
            else:
                match reduced:
                    case Buit():
                        return Buit()
                    case Node(x,Buit(),Buit()):
                        return Node(x,Buit(),Buit())
                    case Node(a,b,c):
                        return Node(a,self.reduce(b),self.reduce(c))
                    case Node("",expi,expd):
                        return Node("",self.reduce(expi),self.reduce(expd))
                    case Node(self.lambda1,expi,Buit()):
                        return Node(self.lambda1,self.reduce(expi),Buit())
        return reduced               
   
    def generarNuevoNombre(self,nombre_original: str, contexto: set) -> str:
        nuevo_nombre = nombre_original
        while nuevo_nombre in contexto:
            if nuevo_nombre == 'z':
                nuevo_nombre = 'a'
            else:
                nuevo_nombre = chr(ord(nuevo_nombre) + 1)
        return nuevo_nombre
    
    def getVarsLibres(self,arbol: Arbre, contexto:set, lligada:set):
        match arbol:
            case Buit():
                return contexto
            case Node(x,Buit(),Buit()):
                if lligada != None and not (x in lligada): 
                    contexto.add(x)
            case Node(self.lambda1,e,d):
                if not isinstance(lligada,set):
                    lligada = set()
                lligada.add(e.val)
                self.getVarsLibres(d,contexto,lligada)
            case Node(self.lambda2,e,d):
                if not isinstance(lligada,set):
                    lligada = set()
                lligada.add(e.val)
                self.getVarsLibres(d,contexto,lligada)
            case Node(x,d,y):
                self.getVarsLibres(d,contexto,lligada)
                self.getVarsLibres(y,contexto,lligada)
                
    def getVars(self,arbol: Arbre, contexto:set):
        #print("getVars: " + abre2String(arbol))
        match arbol:
            case Buit():
                return contexto
            case Node(x,Buit(),Buit()):
                return contexto
            case Node(self.lambda1,e,d):
                contexto.add(e.val)
                self.getVars(d,contexto)
            case Node(self.lambda2,e,d):
                contexto.add(e.val)
                self.getVars(d,contexto)
            case Node(x,d,y):
                self.getVars(d,contexto)
                self.getVars(y,contexto)
    
    def cambiarExp(self,nuevo: str, antiguo:str, arbol: Arbre) -> Arbre:
        match arbol:
            case Buit():
                return Buit()
            case Node(x,Buit(),Buit()):
                if x == antiguo:
                    return Node(nuevo, Buit(), Buit())
                else:
                    return Node(x,Buit(),Buit())
            case Node(self.lambda1,x,y):
                if x.val == antiguo:
                    return Node(self.lambda1,Node(nuevo,Buit(),Buit()),self.cambiarExp(nuevo,antiguo,y))
                else: 
                    return Node(self.lambda1,x,self.cambiarExp(nuevo,antiguo,y))
            case Node(x,e,d):
                return Node(x,self.cambiarExp(nuevo,antiguo,e),self.cambiarExp(nuevo,antiguo,d))
        
    def alphaConvertir(self,arbol: Arbre) -> Arbre:
        contexto = set()
        expres = set()
        lligada = set()
        match arbol:
            case Node("",Node("λ",var,exp),d):
                exp_antigua = Node("λ",var,exp)
                self.getVarsLibres(d,contexto,lligada) #lo de la derecha
                expres.add(var.val)
                self.getVars(exp,expres) #lo de la izquierda
                intersect = contexto.intersection(expres)
                nuevosValores = []  #-> [(viejo,nuevo)...[an,bn]]
                for inter in intersect:
                    nuevo = self.generarNuevoNombre(inter,contexto.union(expres))
                    nuevosValores.append((inter,nuevo))
                    
                    #print("α-conversió: " + inter + " → " + nuevo)
                    expres.add(nuevo)
                    expres.remove(inter)
                    exp_nueva = self.cambiarExp(nuevo,inter,exp_antigua)
                    self.respuesta_evaluada.append((abre2String(exp_antigua) + " → α → " + abre2String(exp_nueva),exp_nueva))
                    arbol = Node("",exp_nueva,d)
        return arbol
    
    def evaluar(self, arbol: Arbre, maxReductions: int = 100) -> list:
        respuesta_evaluada = []
        i = 1
        repe = 0
        reducido = False
        while(i <= maxReductions):
            arbolConver = self.alphaConvertir(arbol)
            reduced = self.reduce(arbolConver)
            if not equal(arbolConver,reduced):
                repe = 0
                arbol = reduced
                reducido = True
            elif equal(arbolConver,reduced) and reducido:
                break
            elif equal(arbolConver,reduced) and repe < 3:
                repe += 1
                self.respuesta_evaluada.append((abre2String(arbol) + " -> β-> " + abre2String(reduced),reduced))
                arbol = reduced
            elif equal(arbolConver,reduced) and repe == 3:
                repe += 1
                self.respuesta_evaluada.append(("...",Buit()))
            elif equal(arbolConver,reduced) and repe >= 4:
                repe += 1
                arbol = reduced
            else :
                break
            i += 1
        self.respuesta_evaluada.append(("Resultat: ",Buit()))
        if repe < 2:
            self.respuesta_evaluada.append((abre2String(arbol),arbol))
        elif i > maxReductions:
            self.respuesta_evaluada.append(("Nothing",Buit()))
        return self.respuesta_evaluada


#Solo tienes que aplicar las alpha a las variables ligadas del terme de la izquierda, que aparecen como libres en el termino de la derecha