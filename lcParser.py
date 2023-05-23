# Generated from lc.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,30,8,2,1,2,0,0,3,0,2,4,0,0,32,0,10,1,0,0,0,2,12,1,0,0,0,4,29,
        1,0,0,0,6,11,3,2,1,0,7,8,3,4,2,0,8,9,5,0,0,1,9,11,1,0,0,0,10,6,1,
        0,0,0,10,7,1,0,0,0,11,1,1,0,0,0,12,13,5,5,0,0,13,14,3,4,2,0,14,3,
        1,0,0,0,15,30,5,6,0,0,16,17,5,2,0,0,17,18,3,4,2,0,18,19,5,3,0,0,
        19,30,1,0,0,0,20,21,5,4,0,0,21,22,5,6,0,0,22,23,5,1,0,0,23,30,3,
        4,2,0,24,25,5,2,0,0,25,26,3,4,2,0,26,27,3,4,2,0,27,28,5,3,0,0,28,
        30,1,0,0,0,29,15,1,0,0,0,29,16,1,0,0,0,29,20,1,0,0,0,29,24,1,0,0,
        0,30,5,1,0,0,0,2,10,29
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'", "<INVALID>", "'?'" ]

    symbolicNames = [ "<INVALID>", "PUNT", "OPAREN", "TPAREN", "LAMBDA", 
                      "INTERROGANTE", "VARIABLE", "WS" ]

    RULE_root = 0
    RULE_arbre = 1
    RULE_expresion = 2

    ruleNames =  [ "root", "arbre", "expresion" ]

    EOF = Token.EOF
    PUNT=1
    OPAREN=2
    TPAREN=3
    LAMBDA=4
    INTERROGANTE=5
    VARIABLE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arbre(self):
            return self.getTypedRuleContext(lcParser.ArbreContext,0)


        def expresion(self):
            return self.getTypedRuleContext(lcParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(lcParser.EOF, 0)

        def getRuleIndex(self):
            return lcParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.arbre()
                pass
            elif token in [2, 4, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.expresion()
                self.state = 8
                self.match(lcParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArbreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)

        def expresion(self):
            return self.getTypedRuleContext(lcParser.ExpresionContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_arbre

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArbre" ):
                return visitor.visitArbre(self)
            else:
                return visitor.visitChildren(self)




    def arbre(self):

        localctx = lcParser.ArbreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arbre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(lcParser.INTERROGANTE)
            self.state = 13
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAREN(self):
            return self.getToken(lcParser.OPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(lcParser.ExpresionContext,0)

        def TPAREN(self):
            return self.getToken(lcParser.TPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(lcParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AplicacionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAREN(self):
            return self.getToken(lcParser.OPAREN, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lcParser.ExpresionContext,i)

        def TPAREN(self):
            return self.getToken(lcParser.TPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacion" ):
                return visitor.visitAplicacion(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lcParser.LAMBDA, 0)
        def VARIABLE(self):
            return self.getToken(lcParser.VARIABLE, 0)
        def PUNT(self):
            return self.getToken(lcParser.PUNT, 0)
        def expresion(self):
            return self.getTypedRuleContext(lcParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccion" ):
                return visitor.visitAbstraccion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self):

        localctx = lcParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expresion)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = lcParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(lcParser.VARIABLE)
                pass

            elif la_ == 2:
                localctx = lcParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(lcParser.OPAREN)
                self.state = 17
                self.expresion()
                self.state = 18
                self.match(lcParser.TPAREN)
                pass

            elif la_ == 3:
                localctx = lcParser.AbstraccionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(lcParser.LAMBDA)
                self.state = 21
                self.match(lcParser.VARIABLE)
                self.state = 22
                self.match(lcParser.PUNT)
                self.state = 23
                self.expresion()
                pass

            elif la_ == 4:
                localctx = lcParser.AplicacionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.match(lcParser.OPAREN)
                self.state = 25
                self.expresion()
                self.state = 26
                self.expresion()
                self.state = 27
                self.match(lcParser.TPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





