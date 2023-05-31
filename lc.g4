grammar lc;

root: (arbre | expresion)* EOF;

arbre: INTERROGANTE expresion           # tree
    ;

expresion: VARIABLE                     # var
    | OPAREN expresion TPAREN           # parentesis
    | expresion expresion               # aplicacion
    | LAMBDA (VARIABLE)+ PUNT expresion # abstraccion
    ;

PUNT : '.' ;
OPAREN : '(' ;
TPAREN : ')' ;
LAMBDA : '\\' | 'λ' ;
INTERROGANTE: '?';
VARIABLE : [a-z] ;
WS : [ \t\n\r]+ -> skip;