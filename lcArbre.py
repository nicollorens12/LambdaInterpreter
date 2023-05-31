
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser
from arbre import Buit
from arbre import Node
from arbre import Arbre



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
        return Node("exp",Buit,Buit)


    # Visit a parse tree produced by lcParser#var.
    def visitVar(self, ctx:lcParser.VarContext):
        [var] = list(ctx.getChildren())
        return Node(var,Buit,Buit)
    
    # Visit a parse tree produced by lcParser#aplicacion.
    def visitAplicacion(self, ctx:lcParser.AplicacionContext):
        [opar,expresion,expresion,tpar] = list(ctx.getChildren())
        return Node("@",self.visit(expresion),self.visit(expresion))


    # Visit a parse tree produced by lcParser#abstraccion.
    def visitAbstraccion(self, ctx:lcParser.AbstraccionContext):
        [lam,var,punt,expresion] = list(ctx.getChildren())
        return Node(lam.getText(),var, self.visit(expresion) )
    

del lcParser