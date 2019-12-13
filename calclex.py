# Projeto da disciplina Linguagens Formais e Tradutores
# Professor André Luis Meneses Silva
# Ano: 2019
# Desenvolvedores: Alcymar, Andeson e Rafael Silveira
# Descrição: Desenvolver um compilador em PYTHON, afim de reconhecer a linguagem ADA

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

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
    'SEMICOLON',
    'COMMENT',
    'DOTDOT',
    'IDENT',
    'ASSIGN',
    'DEDENT',
    'ID'
]+list(palRESERVADA.values())

'''
This is a tuple list, which store code idents. 
tuple structure = (numSpaces,numTabs)
'''
identList = []

# Regular expression rules for simple tokens
t_COMMENT = r'[--][^\n]*\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'"[^--]*"'
t_ASSIGN = r':='
t_COLON = r'\:'
t_SEMICOLON = r';'
t_DOTDOT = r'\.\.'

# A regular expression rule with some action code
# A cada token, uma regra deve ser executada

def t_IDENT(t):
    r'\n[ \t]*'
    if identList.__len__() == 0: # insere o primeiro item da pilha
        identList.append((0,0))
        print(identList)
    spc = t.value.count(' ')
    tab = t.value.count('\t')
    tuplaident = (spc,tab)

    # comparando o topo da pilha com a identação atual
    if identList[-1] > tuplaident:
        identList.pop() # desempilha ident
        print(identList)
        t.type = 'DEDENT'
        return t # retorna dedent

    elif identList[-1] < tuplaident:
        identList.append((spc,tab)) # empilha ident
        print(identList)
        return t

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

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''procedure soma is 
valor: integer
-- Isto é um comentario
begin
    if valor 5..10 loop
    begin
        valor := ((valor + 4) * 10) + (-20 * 2);
        end if
    end loop
end soma;
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)