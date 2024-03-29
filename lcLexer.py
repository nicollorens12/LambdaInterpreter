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
        4,0,11,58,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,4,1,4,1,5,1,5,5,5,36,8,5,10,5,12,5,39,9,5,1,6,4,6,42,8,
        6,11,6,12,6,43,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,53,8,10,11,10,12,
        10,54,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,1,0,8,2,0,92,92,955,955,1,0,97,122,1,0,65,90,3,0,48,57,
        65,90,97,122,1,0,48,57,2,0,61,61,8801,8801,4,0,35,38,42,43,45,45,
        47,47,3,0,9,10,13,13,32,32,60,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,
        0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,0,
        5,27,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,41,1,0,0,
        0,15,45,1,0,0,0,17,47,1,0,0,0,19,49,1,0,0,0,21,52,1,0,0,0,23,24,
        5,46,0,0,24,2,1,0,0,0,25,26,5,40,0,0,26,4,1,0,0,0,27,28,5,41,0,0,
        28,6,1,0,0,0,29,30,7,0,0,0,30,8,1,0,0,0,31,32,7,1,0,0,32,10,1,0,
        0,0,33,37,7,2,0,0,34,36,7,3,0,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,
        1,0,0,0,37,38,1,0,0,0,38,12,1,0,0,0,39,37,1,0,0,0,40,42,7,4,0,0,
        41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,14,1,
        0,0,0,45,46,5,63,0,0,46,16,1,0,0,0,47,48,7,5,0,0,48,18,1,0,0,0,49,
        50,7,6,0,0,50,20,1,0,0,0,51,53,7,7,0,0,52,51,1,0,0,0,53,54,1,0,0,
        0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,6,10,0,0,57,22,
        1,0,0,0,4,0,37,43,54,1,6,0,0
    ]

class lcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PUNT = 1
    OPAREN = 2
    CPAREN = 3
    LAMBDA = 4
    VARIABLE = 5
    IDENTIFIER = 6
    NUMEROS = 7
    INTERROGANTE = 8
    ASSIG = 9
    OPERACION = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'('", "')'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "PUNT", "OPAREN", "CPAREN", "LAMBDA", "VARIABLE", "IDENTIFIER", 
            "NUMEROS", "INTERROGANTE", "ASSIG", "OPERACION", "WS" ]

    ruleNames = [ "PUNT", "OPAREN", "CPAREN", "LAMBDA", "VARIABLE", "IDENTIFIER", 
                  "NUMEROS", "INTERROGANTE", "ASSIG", "OPERACION", "WS" ]

    grammarFileName = "lc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


