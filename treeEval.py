from arbre import *

class functionsArbre:
    
    lambdaChar = "λ"
    lambdaBarra = "\\"
    
    respuesta_evaluada = []
    

    def reduceBeta(self,arbol: Arbre) -> Arbre:
        match arbol:
            case Buit():
                return Buit
            case Node("",Node("\\",a,b),d):
                return self.substituir(a,b,d)
            case Node("",Node("λ",a,b),d):
                return self.substituir(a,b,d)
            case _:
                return arbol
    
    def substituir(self, arbol: Arbre, var: Arbre, argud: Arbre) -> Arbre:
        match var:
            case Node(x, Buit(),Buit()):
                if arbol.val == x:
                    return argud
                else:
                    return var
            case Node(x,i,d):
                new_i = self.substituir(arbol,i,argud)
                new_d = self.substituir(arbol,d,argud)
                return Node(x,new_i,new_d)
            case _:
                return arbol

    def reduce(self, arbol: Arbre) -> Arbre:
        if arbol != None and arbol != Buit():
            reduced = self.reduceBeta(arbol)
            if not equal(reduced,arbol):
                self.respuesta_evaluada.append((abre2String(arbol) + " -> β-> " + abre2String(reduced),reduced))
                
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
                    case Node(self.lambdaChar,expi,Buit()):
                        return Node(self.lambdaChar,self.reduce(expi),Buit())
        return reduced               
   
    def charGen(self,nombre_original: str, contexto: set) -> str:
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
            case Node(self.lambdaChar,e,d):
                if not isinstance(lligada,set):
                    lligada = set()
                lligada.add(e.val)
                self.getVarsLibres(d,contexto,lligada)
            case Node(self.lambdaBarra,e,d):
                if not isinstance(lligada,set):
                    lligada = set()
                lligada.add(e.val)
                self.getVarsLibres(d,contexto,lligada)
            case Node(x,d,y):
                self.getVarsLibres(d,contexto,lligada)
                self.getVarsLibres(y,contexto,lligada)
                
    def getVars(self,arbol: Arbre, contexto:set):
        match arbol:
            case Buit():
                return contexto
            case Node(x,Buit(),Buit()):
                return contexto
            case Node(self.lambdaChar,e,d):
                contexto.add(e.val)
                self.getVars(d,contexto)
            case Node(self.lambdaBarra,e,d):
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
            case Node(self.lambdaChar,x,y):
                if x.val == antiguo:
                    return Node(self.lambdaChar,Node(nuevo,Buit(),Buit()),self.cambiarExp(nuevo,antiguo,y))
                else: 
                    return Node(self.lambdaChar,x,self.cambiarExp(nuevo,antiguo,y))
            case Node(x,e,d):
                return Node(x,self.cambiarExp(nuevo,antiguo,e),self.cambiarExp(nuevo,antiguo,d))
        
    def aConvert(self,arbol: Arbre) -> Arbre:
        contexto = set()
        expres = set()
        lligada = set()
        match arbol:
            case Node("",Node("λ",var,exp),d):
                exp_antigua = Node("λ",var,exp)
                self.getVarsLibres(d,contexto,lligada)
                expres.add(var.val)
                self.getVars(exp,expres) 
                intersect = contexto.intersection(expres)
                nuevosValores = []  
                for inter in intersect:
                    nuevo = self.charGen(inter,contexto.union(expres))
                    nuevosValores.append((inter,nuevo))
                    
                    expres.add(nuevo)
                    expres.remove(inter)
                    exp_nueva = self.cambiarExp(nuevo,inter,exp_antigua)
                    self.respuesta_evaluada.append((abre2String(exp_antigua) + " → α → " + abre2String(exp_nueva),exp_nueva))
                    arbol = Node("",exp_nueva,d)
        return arbol
    
    def evaluar(self, arbol: Arbre, maxRed: int = 20) -> list:
        respuesta_evaluada = []
        i = 1
        repe = 0
        reducido = False
        while(i <= maxRed):
            arbolConver = self.aConvert(arbol)
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
        #self.respuesta_evaluada.append(("Resultat: ",Buit()))
        if repe < 2:
            self.respuesta_evaluada.append((abre2String(arbol),arbol))
        elif i > maxRed:
            self.respuesta_evaluada.append(("Nothing",Buit()))
        return self.respuesta_evaluada
