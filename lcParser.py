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
        4,1,7,35,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,5,0,9,8,0,10,0,12,0,12,
        9,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,33,8,2,1,2,0,0,3,0,2,4,0,0,36,0,10,1,0,0,0,2,
        15,1,0,0,0,4,32,1,0,0,0,6,9,3,2,1,0,7,9,3,4,2,0,8,6,1,0,0,0,8,7,
        1,0,0,0,9,12,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,0,11,13,1,0,0,0,12,
        10,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,5,0,0,16,17,3,4,2,
        0,17,3,1,0,0,0,18,33,5,6,0,0,19,20,5,2,0,0,20,21,3,4,2,0,21,22,5,
        3,0,0,22,33,1,0,0,0,23,24,5,4,0,0,24,25,5,6,0,0,25,26,5,1,0,0,26,
        33,3,4,2,0,27,28,5,2,0,0,28,29,3,4,2,0,29,30,3,4,2,0,30,31,5,3,0,
        0,31,33,1,0,0,0,32,18,1,0,0,0,32,19,1,0,0,0,32,23,1,0,0,0,32,27,
        1,0,0,0,33,5,1,0,0,0,3,8,10,32
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

        def EOF(self):
            return self.getToken(lcParser.EOF, 0)

        def arbre(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ArbreContext)
            else:
                return self.getTypedRuleContext(lcParser.ArbreContext,i)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lcParser.ExpresionContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 116) != 0):
                self.state = 8
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 6
                    self.arbre()
                    pass
                elif token in [2, 4, 6]:
                    self.state = 7
                    self.expresion()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 13
            self.match(lcParser.EOF)
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


        def getRuleIndex(self):
            return lcParser.RULE_arbre

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TreeContext(ArbreContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ArbreContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)
        def expresion(self):
            return self.getTypedRuleContext(lcParser.ExpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTree" ):
                return visitor.visitTree(self)
            else:
                return visitor.visitChildren(self)



    def arbre(self):

        localctx = lcParser.ArbreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arbre)
        try:
            localctx = lcParser.TreeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(lcParser.INTERROGANTE)
            self.state = 16
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = lcParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(lcParser.VARIABLE)
                pass

            elif la_ == 2:
                localctx = lcParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(lcParser.OPAREN)
                self.state = 20
                self.expresion()
                self.state = 21
                self.match(lcParser.TPAREN)
                pass

            elif la_ == 3:
                localctx = lcParser.AbstraccionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(lcParser.LAMBDA)
                self.state = 24
                self.match(lcParser.VARIABLE)
                self.state = 25
                self.match(lcParser.PUNT)
                self.state = 26
                self.expresion()
                pass

            elif la_ == 4:
                localctx = lcParser.AplicacionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.match(lcParser.OPAREN)
                self.state = 28
                self.expresion()
                self.state = 29
                self.expresion()
                self.state = 30
                self.match(lcParser.TPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





