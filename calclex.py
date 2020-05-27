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

# tamanho padrão para tabs neste compilador
# pode ser alterado na GUI

tabSize = 4

#revisar palavras
palRESERVADA =  {
    'and' : 'AND',
    'array' : 'ARRAY',
    'begin' : 'BEGIN', 
    'else' : 'ELSE',
    'elsif' : 'ELSIF',
    'end' : 'END',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'procedure' : 'PROCEDURE',
    'if' : 'IF',
    'in' : 'IN',
    'is' : 'IS',
    'loop' : 'LOOP',
    'of' : 'OF',
    'or' : 'OR',
    'puts' : 'PUTS',
    'return' : 'RETURN',
    'then' : 'THEN',
    'while' : 'WHILE',
  }

# List of token names. This is always required
tokens = [
    'NUMBER_INT',
    'NUMBER_FLOAT',
    'NUMBER_EXPONENT',
    'BOOLEAN',
    'CHAR',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'STRING',
    'COMMA',
    'COLON',
    'TYPE',
    'SEMICOLON',
    'DOTDOT',
    'ASSIGN', 
    'GREATERTHAN',
    'GREATERTHANEQUAL',
    'LESSTHAN',
    'LESSTHANEQUAL',
    'NOTEQUAL',
    'EQUAL',
    'ID'
]+list(palRESERVADA.values())

'''
This is a tuple list, which store code idents. 
tuple structure = (numSpaces,numTabs)
'''
identList = []

# Regular expression rules for simple tokens
t_ignore_COMMENT = r'--[^\n]*\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'"[^--]*"'
t_CHAR  = r"'[^\r\n\t\f]'"
t_ASSIGN = r':='
t_COMMA = r','
t_COLON = r'\:'
t_SEMICOLON = r';'
t_GREATERTHAN = r'>'
t_GREATERTHANEQUAL = r'>='
t_LESSTHAN = r'<'
t_LESSTHANEQUAL = r'<='
t_NOTEQUAL = r'/='
t_EQUAL = r'='
t_DOTDOT = r'\.\.'
t_BOOLEAN = r'true|false'
t_TYPE = r'Integer|Float|Character|String|Boolean'

def t_IDENT(t):
    r'\n[ \t]*'
    counter = 0
    if identList.__len__() == 0: # insere o primeiro item da pilha
        identList.append(counter)
        print(identList)
    for i in range(0,len(t.value)):
    	if t.value[i] == ' ':
    		counter += 1
    	# deve ser feito num laço
    	elif t.value[i] == '/t':
    		counter += tabSize-(counter % tabSize)
 
    # comparando o topo da pilha com a identação atual
    if identList[-1] > counter:
        #não existe do-while em python
        while True:
            identList.pop() #desempilha ident
            if identList[-1] > counter:   # contador menor que a pilha = houve uma dedentação múltipla
                continue
            elif identList[-1] < counter: # contador maior que a pilha = erro no dedent
                print('Erro de identação')
                break 
            else: 						# contador igual a pilha = identação OK
                break
        print(identList)  
          
    elif identList[-1] < counter:
        identList.append(counter) # empilha ident
        print(identList)



def t_NUMBER_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER_EXPONENT(t):
    r'\d+E[+-]\d+|\d+\.\d+E[+-]\d+'
    t.value = float(t.value)
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

#sourceCode = open('progExemplo.adc','r')
#data = sourceCode.read()
data = ''
sourceCode = open('progExemplo.adb','r')
data = sourceCode.read()

# Give the lexer some input
lexer.input(data)

# Tokenize