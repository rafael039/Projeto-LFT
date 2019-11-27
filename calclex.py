# Projeto da disciplina Linguagens Formais e Tradutores
# Professor André Luis Meneses Silva
# Ano: 2019
# Desenvolvedores: Alcymar, Andeson e Rafael Silveira
# Descrição: Desenvolver um compilador em PYTHON, afim de reconhecer a linguagem ADA

# ------------------------------------------------------------
# calclex.py
 #
#tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex
#dicionário

palRESERVADA =  {
    'abs' : 'ABS',
    'aliased' : 'ALIASED',
    'and' : 'AND',
    'array' : 'ARRAY',
    'begin' : 'BEGIN',
    'body' : 'BODY',
    'case' : "CASE",
    'constant' : 'CONSTANT',
    'declare' : 'DECLARE',
    'digits' : 'DIGITS',
    'do' : 'DO',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'end' : 'END',
    'exit' : 'EXIT',
    'false' : 'FALSE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'if' : 'IF',
    'loop' : 'LOOP',
    'mod' : 'MOD',
    'not' : 'NOT',
    'null' : 'NULL',
    'of' : 'OF',
    'or' : 'OR',
    'procedure' : 'PROCEDURE',
    'raise' : 'RAISE',
    'range' : 'RANGE',
    'repeat' : 'REPEAT',
    'return' : 'RETURN',
    'reverse' : 'REVERSE',
    'task' : 'TASK',
    'then' : 'THEN',
    'true' : 'TRUE',
    'use' : 'USE',
    'while' : 'WHILE',
    'xor' : 'XOR'}

# List of token names. This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'STRING',
    'COLON',
    'DOTDOT',
    'IDENT',
    'DEDENT',
    'ID'
]+list(palRESERVADA.values())

''' tuple structure = (numSpaces,numTabs)'''
identList = []


# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'"[^--]*"'
t_COLON = r'\:'
t_DOTDOT = r'\.\.'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palRESERVADA.get(t.value,'ID') # Check for reserved words
    return t

def t_IDENT(t):
    r'[\n][ \t]+'
    spc = t.value.count(' ')
    tab = t.value.count('\t')
    identList.append((spc,tab))
    return t


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
     procedure soma is 
     valor: integer
     begin 
        ((3 + 4) * 10) + (-20 * 2)  
     end soma
     
    PROCEDURE REPETICAO IS
    CONTADOR : INTEGER
    BEGIN
    
    FOR CONTADOR IN 1 .. 10 LOOP
    END LOOP
    
      END REPETICAO     
    
    
     
     '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)

