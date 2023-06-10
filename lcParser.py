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
        4,1,11,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,27,
        8,1,10,1,12,1,30,9,1,1,1,1,1,4,1,34,8,1,11,1,12,1,35,3,1,38,8,1,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,51,8,3,11,3,12,3,
        52,1,3,1,3,3,3,57,8,3,1,3,1,3,5,3,61,8,3,10,3,12,3,64,9,3,1,3,0,
        1,6,4,0,2,4,6,0,1,2,0,6,6,10,10,72,0,13,1,0,0,0,2,37,1,0,0,0,4,39,
        1,0,0,0,6,56,1,0,0,0,8,12,3,2,1,0,9,12,3,4,2,0,10,12,3,6,3,0,11,
        8,1,0,0,0,11,9,1,0,0,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,
        13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,
        0,0,18,19,5,8,0,0,19,20,7,0,0,0,20,21,5,9,0,0,21,38,3,6,3,0,22,23,
        5,8,0,0,23,28,5,6,0,0,24,25,5,10,0,0,25,27,5,6,0,0,26,24,1,0,0,0,
        27,30,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,38,1,0,0,0,30,28,1,
        0,0,0,31,33,5,8,0,0,32,34,5,6,0,0,33,32,1,0,0,0,34,35,1,0,0,0,35,
        33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,18,1,0,0,0,37,22,1,0,0,
        0,37,31,1,0,0,0,38,3,1,0,0,0,39,40,5,8,0,0,40,41,3,6,3,0,41,5,1,
        0,0,0,42,43,6,3,-1,0,43,57,5,5,0,0,44,45,5,2,0,0,45,46,3,6,3,0,46,
        47,5,3,0,0,47,57,1,0,0,0,48,50,5,4,0,0,49,51,5,5,0,0,50,49,1,0,0,
        0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,
        5,1,0,0,55,57,3,6,3,1,56,42,1,0,0,0,56,44,1,0,0,0,56,48,1,0,0,0,
        57,62,1,0,0,0,58,59,10,2,0,0,59,61,3,6,3,3,60,58,1,0,0,0,61,64,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,7,1,0,0,0,64,62,1,0,0,0,8,11,
        13,28,35,37,52,56,62
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'?'" ]

    symbolicNames = [ "<INVALID>", "PUNT", "OPAREN", "CPAREN", "LAMBDA", 
                      "VARIABLE", "IDENTIFIER", "NUMEROS", "INTERROGANTE", 
                      "ASSIG", "OPERACION", "WS" ]

    RULE_root = 0
    RULE_macro = 1
    RULE_arbol = 2
    RULE_terme = 3

    ruleNames =  [ "root", "macro", "arbol", "terme" ]

    EOF = Token.EOF
    PUNT=1
    OPAREN=2
    CPAREN=3
    LAMBDA=4
    VARIABLE=5
    IDENTIFIER=6
    NUMEROS=7
    INTERROGANTE=8
    ASSIG=9
    OPERACION=10
    WS=11

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

        def macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.MacroContext)
            else:
                return self.getTypedRuleContext(lcParser.MacroContext,i)


        def arbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.ArbolContext)
            else:
                return self.getTypedRuleContext(lcParser.ArbolContext,i)


        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 308) != 0):
                self.state = 11
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.macro()
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.arbol()
                    pass

                elif la_ == 3:
                    self.state = 10
                    self.terme(0)
                    pass


                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(lcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MacroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_macro

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MacroAssigContext(MacroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.MacroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)
        def ASSIG(self):
            return self.getToken(lcParser.ASSIG, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)

        def IDENTIFIER(self):
            return self.getToken(lcParser.IDENTIFIER, 0)
        def OPERACION(self):
            return self.getToken(lcParser.OPERACION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroAssig" ):
                return visitor.visitMacroAssig(self)
            else:
                return visitor.visitChildren(self)


    class MacroOpContext(MacroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.MacroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.IDENTIFIER)
            else:
                return self.getToken(lcParser.IDENTIFIER, i)
        def OPERACION(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.OPERACION)
            else:
                return self.getToken(lcParser.OPERACION, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroOp" ):
                return visitor.visitMacroOp(self)
            else:
                return visitor.visitChildren(self)


    class MacroApliContext(MacroContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.MacroContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.IDENTIFIER)
            else:
                return self.getToken(lcParser.IDENTIFIER, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacroApli" ):
                return visitor.visitMacroApli(self)
            else:
                return visitor.visitChildren(self)



    def macro(self):

        localctx = lcParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_macro)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = lcParser.MacroAssigContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(lcParser.INTERROGANTE)
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==6 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.match(lcParser.ASSIG)
                self.state = 21
                self.terme(0)
                pass

            elif la_ == 2:
                localctx = lcParser.MacroOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(lcParser.INTERROGANTE)
                self.state = 23
                self.match(lcParser.IDENTIFIER)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 24
                    self.match(lcParser.OPERACION)
                    self.state = 25
                    self.match(lcParser.IDENTIFIER)
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                localctx = lcParser.MacroApliContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(lcParser.INTERROGANTE)
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 32
                    self.match(lcParser.IDENTIFIER)
                    self.state = 35 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_arbol

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArbolFContext(ArbolContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.ArbolContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTERROGANTE(self):
            return self.getToken(lcParser.INTERROGANTE, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArbolF" ):
                return visitor.visitArbolF(self)
            else:
                return visitor.visitChildren(self)



    def arbol(self):

        localctx = lcParser.ArbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arbol)
        try:
            localctx = lcParser.ArbolFContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(lcParser.INTERROGANTE)
            self.state = 40
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAREN(self):
            return self.getToken(lcParser.OPAREN, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)

        def CPAREN(self):
            return self.getToken(lcParser.CPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lcParser.LAMBDA, 0)
        def PUNT(self):
            return self.getToken(lcParser.PUNT, 0)
        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.VARIABLE)
            else:
                return self.getToken(lcParser.VARIABLE, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(lcParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class AplContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApl" ):
                return visitor.visitApl(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = lcParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(lcParser.VARIABLE)
                pass
            elif token in [2]:
                localctx = lcParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(lcParser.OPAREN)
                self.state = 45
                self.terme(0)
                self.state = 46
                self.match(lcParser.CPAREN)
                pass
            elif token in [4]:
                localctx = lcParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(lcParser.LAMBDA)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 49
                    self.match(lcParser.VARIABLE)
                    self.state = 52 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==5):
                        break

                self.state = 54
                self.match(lcParser.PUNT)
                self.state = 55
                self.terme(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lcParser.AplContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 58
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 59
                    self.terme(3) 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




