from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from lcArbre import lcArbre

input_stream = FileStream("input.txt", encoding='utf-8')
lexer = lcLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lcParser(token_stream)
tree = parser.root()


print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))

visitor = lcVisitor()
visitor.visit(tree)

arbol = lcArbre()
arbol.create(tree)
#a.toString()