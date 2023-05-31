from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from lcArbre import lcArbre
from arbre import *

input_stream = FileStream("input.txt", encoding='utf-8')
lexer = lcLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lcParser(token_stream)
tree = parser.root()

#print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))


arbol = lcArbre()
arbol.visit(tree)

arbs = arbol.arboles

for arbol in arbs:
    resultado = arbre2String(arbol)
    print(resultado)
    
#a.toString()