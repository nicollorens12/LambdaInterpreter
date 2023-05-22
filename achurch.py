from antlr4 import *
from lcLexer import exprsLexer
from lcParser import exprsParser

input_stream = FileStream(sys.argv[1], encoding='utf-8')
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))