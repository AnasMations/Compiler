############### Lexemes and Tokens

"LEXEME": "TOKEN",
"INT": "int", 
"FLOAT": "float",
"DOUBLE": "double",
"BOOL": "bool",
"STRING": "string",
"CHAR": "char",
"SET": "set",
"IF": "if",
"THEN": "then",
"ELSE": "else",
"FOR": "for",
"WHILE": "while",
"DO": "do",
"ENDWHILE": "endwhile",
"UNTIL": "until",
"ENDUNTIL": "enduntil",
"CALL": "call",
"+": "+",
"-": "-",
"*": "*",
"/": "/",
"=": "=",
">": ">",
"<": "<",
"==": "==",
"<=": "<=",
">=": ">=",
"!=": "!=",
"ENDIF": "endif",


############### CFG Rules

# Main rules
Program -> statements_block
statements_block -> statements statements_block | ε
statements -> declare_statement | set_statement | expression | if_statement | while_statement | function | read_statement | write_statement

# Main statements
declare_statement -> type id

set_statement -> 'set' id '=' expression

if_statement -> 'if' condition 'then' statements_block 'else' statements_block 'endif'

while_statement -> 'while' condition 'do' statements_block 'endwhile'

function -> 'function' id '(' id ')' statements_block 'endfunction'

read_statement -> 'read' id

write_statement -> 'write' expression

# Expressions
expression -> term arth_op term
arth_op -> '+' | '-' | '*' | '/'
term -> id | number

# Conditions
condition -> expression rel_op expression
rel_op -> '<' | '<=' | '>' | '>=' | '==' | '!='

# Types
type -> 'int' | 'float' | 'double' | 'bool' | 'string' | 'char'
id -> identifier
number -> constant

############### sample code

int x
int y
set x = 1
if x > 2 then 
    y = x + 2
else
    y = x + 5
endif

############### Lexemes

Lexeme: INT
Lexeme: x
Lexeme: INT
Lexeme: y
Lexeme: SET
Lexeme: x
Lexeme: =
Lexeme: 1
Lexeme: IF
Lexeme: x
Lexeme: >
Lexeme: 2
Lexeme: THEN
Lexeme: y
Lexeme: =
Lexeme: x
Lexeme: +
Lexeme: 2
Lexeme: ELSE
Lexeme: y
Lexeme: =
Lexeme: x
Lexeme: +
Lexeme: 5
Lexeme: ENDIF

INT x INT y SET x = 1 IF x > 2 THEN y = x + 2 ELSE y = x + 5 ENDIF $

############### Parse Tree

Program
|-- statements_block
| |-- declare_statement
| | |-- int: INT
| | |-- id: x
| | |-- int: INT
| | |-- id: y
| |-- assign_statement
| | |-- set: SET
| | |-- id: x
| | |-- equal: =
| | |-- number: 1
| |-- if_statement
| | |-- if: IF
| | |-- condition
| | | |-- id: x
| | | |-- operation: >
| | | |-- number: 2
| | |-- then_statement
| | | |-- then: THEN
| | | |-- statements
| | | | |-- id: y
| | | | |-- equal: =
| | | | |-- id: x
| | | | |-- operation: +
| | | | |-- number: 2
| | |-- else_statement
| | | |-- else: ELSE
| | | |-- statements
| | | | |-- id: y
| | | | |-- equal: =
| | | | |-- id: x
| | | | |-- operation: +
| | | | |-- number: 5
| | | -- endif: ENDIF
|-- End

