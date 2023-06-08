from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from lcArbre import lcArbre
from arbre import *
from reductor import *
from Evaluador import funcionsEvaluador

input_stream = FileStream("input.txt", encoding='utf-8')
lexer = lcLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lcParser(token_stream)
tree = parser.root()
evaluador = funcionsEvaluador()


arbol = lcArbre()
arbol.visit(tree)

arbs = arbol.arboles

for arbol in arbs:
    arb = arbol
    arbolstr = arbre2String(arb)
    print("Arbre: ")
    print(arbolstr)
    evaluador.evaluarExp(arb)
    print("")
    
    
#a.toString()