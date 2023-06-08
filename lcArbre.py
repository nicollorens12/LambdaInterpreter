
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser
from arbre import *

class lcArbre(ParseTreeVisitor):

    def __init__(self):
        self.arboles = []

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by lcParser#tree.
    def visitTree(self, ctx:lcParser.TreeContext):
        #lista((terme,arbol))
        [interrogante, expresion] = list(ctx.getChildren())
        self.arboles.append(self.visit(expresion)) 
    
    # Visit a parse tree produced by lcParser#parentesis.
    def visitParentesis(self, ctx:lcParser.ParentesisContext):
        [opar,expresion,tpar] = list(ctx.getChildren())
        return self.visit(expresion)


    # Visit a parse tree produced by lcParser#var.
    def visitVar(self, ctx:lcParser.VarContext):
        [var] = list(ctx.getChildren())
        return Node(var.getText(),Buit(),Buit())
    
    # Visit a parse tree produced by lcParser#aplicacion.
    def visitAplicacion(self, ctx:lcParser.AplicacionContext):
        [expresion1,expresion2] = list(ctx.getChildren())
        return Node("",self.visit(expresion1),self.visit(expresion2))


    # Visit a parse tree produced by lcParser#abstraccion.
    def visitAbstraccion(self, ctx:lcParser.AbstraccionContext):
        abstr = list(ctx.getChildren())
        lam = abstr[0].getText()
        arbre = None
        size = len(abstr)
        for i in range(size -1,0,-1):
            if(i == size -1):
                arbre = self.visit(abstr[i])
            elif(i < size - 2):
                arbre = Node(lam,Node(abstr[i].getText(),Buit(),Buit()),arbre)
        return arbre
    

del lcParser