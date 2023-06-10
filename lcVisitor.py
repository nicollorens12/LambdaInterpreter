# Generated from lc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macroAssig.
    def visitMacroAssig(self, ctx:lcParser.MacroAssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macroOp.
    def visitMacroOp(self, ctx:lcParser.MacroOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macroApli.
    def visitMacroApli(self, ctx:lcParser.MacroApliContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#arbolF.
    def visitArbolF(self, ctx:lcParser.ArbolFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#paren.
    def visitParen(self, ctx:lcParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#abs.
    def visitAbs(self, ctx:lcParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#var.
    def visitVar(self, ctx:lcParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#apl.
    def visitApl(self, ctx:lcParser.AplContext):
        return self.visitChildren(ctx)



del lcParser