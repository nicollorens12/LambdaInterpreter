from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser
from arbre import *

class lcVisitorArbol(ParseTreeVisitor):
    
    def __init__(self):
        self.mapMacros = {}
        self.arboles = []

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)
    
    
    def visitArbolF(self, ctx:lcParser.ArbolFContext):
        [_,terme] = list(ctx.getChildren())
        arbol = self.visit(terme)
        self.arboles.append((terme.getText(),arbol))

    # Visit a parse tree produced by lcParser#paren.
    def visitParen(self, ctx:lcParser.ParenContext):
        [_,terme,_] = list(ctx.getChildren())
        return self.visit(terme)


    # Visit a parse tree produced by lcParser#abs.
    def visitAbs(self, ctx:lcParser.AbsContext):
        #Lxy.z == Lx.Ly.z
        lams = list(ctx.getChildren())
        lamda = lams[0].getText()
        arbre = Buit()
        for i in range(len(lams)- 1, 0,-1):
            if(i == len(lams)- 1):
                arbre = self.visit(lams[i])
            elif(i < len(lams)- 2):
                arbre = Node(lamda,Node(lams[i].getText(),Buit(),Buit()),arbre)
        return arbre


    # Visit a parse tree produced by lcParser#var.
    def visitVar(self, ctx:lcParser.VarContext):
        [var] = list(ctx.getChildren())
        return Node(var.getText(), Buit(),Buit())


    # Visit a parse tree produced by lcParser#apl.
    def visitApl(self, ctx:lcParser.AplContext):
        [terme1, terme2] = list(ctx.getChildren())
        izquierdo = self.visit(terme1)
        derecho = self.visit(terme2)
        return Node("",izquierdo, derecho)
    
    def visitMacroAssig(self, ctx:lcParser.MacroAssigContext):
        [_,identificador,_,terme] = list(ctx.getChildren())
        self.mapMacros[identificador.getText()] = self.visit(terme)
    
    def visitMacroApli(self, ctx:lcParser.MacroAssigContext):

        macros  = list(ctx.getChildren())
        strMacro = ""
        arbol_out = Node("",Buit(),Buit())

        for i in range(len(macros)- 1, 0,-1):
            strMacro += macros[i].getText() + " "
            if equal(arbol_out.dre,Buit()):
                #print("1: " + macros[i].getText())
                arbol_out.dre = self.mapMacros[macros[i].getText()]
            elif equal(arbol_out.esq,Buit()):
                #print("2: " + macros[i].getText())
                arbol_out.esq = self.mapMacros[macros[i].getText()]
            else:
                arbol_out = Node("",self.mapMacros[macros[i].getText()],arbol_out)
        self.arboles.append((strMacro,arbol_out))
        
    def visitMacroOp(self, ctx:lcParser.MacroOpContext): 
        macros  = list(ctx.getChildren())
        strMacro = ""
        arbol_out = Node("",Buit(),Buit())

        for macro in macros[1:]:
            strMacro += macro.getText() + " "
            if equal(arbol_out.dre,Buit()):
                #print("1: " + macro.getText())
                arbol_out.dre = self.mapMacros[macro.getText()]
            elif equal(arbol_out.esq,Buit()):
                #print("2: " + macro.getText())
                arbol_out.esq = self.mapMacros[macro.getText()]
            else:
                arbol_out = Node("",arbol_out,self.mapMacros[macro.getText()])
        self.arboles.append((strMacro,arbol_out))
