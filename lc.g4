grammar lc;

root: terme EOF;

terme: VARIABLE
    | OPAREN terme TPAREN
    | LAMBDA VARIABLE PUNT
    | terme terme
    ;

PUNT : '.' ;
OPAREN : '(' ;
TPAREN : ')' ;
LAMBDA : '\\' | 'λ' ;
VARIABLE : [a-z] ;
WS : [ \t\n\r]+ -> skip;