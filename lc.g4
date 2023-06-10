grammar lc;

root:  (macro |arbol | terme)* EOF ;

macro: INTERROGANTE (IDENTIFIER|OPERACION) ASSIG terme                           #macroAssig
    | INTERROGANTE IDENTIFIER  (OPERACION IDENTIFIER)*                #macroOp
    | INTERROGANTE (IDENTIFIER)+                                     #macroApli
    ;

arbol: INTERROGANTE terme                               #arbolF   
    ;

terme: VARIABLE                                         #var
    | OPAREN terme CPAREN                               #paren
    | terme terme                                       #apl
    | LAMBDA (VARIABLE)+ PUNT terme                     #abs
    ;

PUNT : '.' ;
OPAREN : '(' ;
CPAREN : ')' ;
LAMBDA : '\\' | 'λ' ;
VARIABLE : [a-z] ;
IDENTIFIER: [A-Z][a-zA-Z0-9]*;
NUMEROS : [0-9]+ ;
INTERROGANTE : '?' ;
ASSIG : '≡' | '=';
OPERACION : '+' | '-' | '*' | '/' | '%' | '$' | '&' | '#' ;
WS: [ \t\n\r]+ -> skip;