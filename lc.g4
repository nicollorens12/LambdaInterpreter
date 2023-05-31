grammar lc;

root: (arbre | expresion)* EOF;

arbre: INTERROGANTE expresion           # tree
    ;

expresion: VARIABLE                     # var
    | OPAREN expresion TPAREN           # parentesis
    | LAMBDA VARIABLE PUNT expresion    # abstraccion
    | OPAREN expresion expresion TPAREN # aplicacion
    ;

PUNT : '.' ;
OPAREN : '(' ;
TPAREN : ')' ;
LAMBDA : '\\' | 'λ' ;
INTERROGANTE: '?';
VARIABLE : [a-z] ;
WS : [ \t\n\r]+ -> skip;