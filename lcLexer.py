# Generated from lc.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,30,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,25,8,5,11,5,12,5,26,
        1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,3,2,0,92,92,955,955,1,
        0,97,122,3,0,9,10,13,13,32,32,30,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,15,1,0,0,
        0,5,17,1,0,0,0,7,19,1,0,0,0,9,21,1,0,0,0,11,24,1,0,0,0,13,14,5,46,
        0,0,14,2,1,0,0,0,15,16,5,40,0,0,16,4,1,0,0,0,17,18,5,41,0,0,18,6,
        1,0,0,0,19,20,7,0,0,0,20,8,1,0,0,0,21,22,7,1,0,0,22,10,1,0,0,0,23,
        25,7,2,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,
        0,27,28,1,0,0,0,28,29,6,5,0,0,29,12,1,0,0,0,2,0,26,1,6,0,0
    ]

class lcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PUNT = 1
    OPAREN = 2
    TPAREN = 3
    LAMBDA = 4
    VARIABLE = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PUNT", "OPAREN", "TPAREN", "LAMBDA", "VARIABLE", "WS" ]

    ruleNames = [ "PUNT", "OPAREN", "TPAREN", "LAMBDA", "VARIABLE", "WS" ]

    grammarFileName = "lc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


