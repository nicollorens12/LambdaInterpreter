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
        4,1,6,26,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,17,8,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,0,1,2,
        2,0,2,0,0,26,0,4,1,0,0,0,2,16,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,
        1,1,0,0,0,7,8,6,1,-1,0,8,17,5,5,0,0,9,10,5,2,0,0,10,11,3,2,1,0,11,
        12,5,3,0,0,12,17,1,0,0,0,13,14,5,4,0,0,14,15,5,5,0,0,15,17,5,1,0,
        0,16,7,1,0,0,0,16,9,1,0,0,0,16,13,1,0,0,0,17,22,1,0,0,0,18,19,10,
        1,0,0,19,21,3,2,1,2,20,18,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,
        23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,2,16,22
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PUNT", "OPAREN", "TPAREN", "LAMBDA", 
                      "VARIABLE", "WS" ]

    RULE_root = 0
    RULE_terme = 1

    ruleNames =  [ "root", "terme" ]

    EOF = Token.EOF
    PUNT=1
    OPAREN=2
    TPAREN=3
    LAMBDA=4
    VARIABLE=5
    WS=6

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

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def EOF(self):
            return self.getToken(lcParser.EOF, 0)

        def getRuleIndex(self):
            return lcParser.RULE_root




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.terme(0)
            self.state = 5
            self.match(lcParser.EOF)
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

        def VARIABLE(self):
            return self.getToken(lcParser.VARIABLE, 0)

        def OPAREN(self):
            return self.getToken(lcParser.OPAREN, 0)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


        def TPAREN(self):
            return self.getToken(lcParser.TPAREN, 0)

        def LAMBDA(self):
            return self.getToken(lcParser.LAMBDA, 0)

        def PUNT(self):
            return self.getToken(lcParser.PUNT, 0)

        def getRuleIndex(self):
            return lcParser.RULE_terme



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 8
                self.match(lcParser.VARIABLE)
                pass
            elif token in [2]:
                self.state = 9
                self.match(lcParser.OPAREN)
                self.state = 10
                self.terme(0)
                self.state = 11
                self.match(lcParser.TPAREN)
                pass
            elif token in [4]:
                self.state = 13
                self.match(lcParser.LAMBDA)
                self.state = 14
                self.match(lcParser.VARIABLE)
                self.state = 15
                self.match(lcParser.PUNT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lcParser.TermeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 18
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 19
                    self.terme(2) 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




