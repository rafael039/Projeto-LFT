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
    'body' : 'BODY', #pode ser eliminado
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
t_COMMENT = r'--[^\n]*\n'
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
        return t

             
'''
     identList.pop() # desempilha ident
        # se a identação for diferente do topo atual da pilha = identação errada
        if identList[-1] != counter:
            print('Erro de identação')
        else :
            -- Isto é um comentario
            t.type = 'DEDENT'
            return t # retorna dedent
'''
    

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

<<<<<<< HEAD
#sourceCode = open('progExemplo.adc','r')
#data = sourceCode.read()
data = ''
=======
sourceCode = open('progExemplo.adb','r')
data = sourceCode.read()

>>>>>>> c526421258accc5c443242eda3f685f4c0a15b57
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break # No more input
    print(tok)