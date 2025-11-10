grammar Grammar;

program:(statement NEWLINE)*EOF;

statement:assing|print|if_statement|for_statement;
/*Definimos la asignacion*/
assing:ID '=' expr;

/*Definimos print*/
print:'print''('expr')';

/*Definimos if*/
if_statement:'if''('expr')'block;

/*Definimos for*/
for_statement:'for''('assing';'expr';'assing')'block;

/*Definimos block*/
block:'{'(statement NEWLINE)*'}';

/*Definimos expr*/

expr:expr op=('*'|'/')expr
    |expr op=('+'|'-')expr
    |expr op=('>'|'<'|'>='|'<=')expr
    |expr op=('=='|'!=')expr
    |ID
    |'('expr)'
    ;

/*Definicion de elementos finales*/

ID:[a-zA-Z][a-zA-Z0-9]*;
NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';