import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
import visitor as vis

def p_program(p):
    '''program : PROCEDURE ID IS decl body
               | PROCEDURE ID IS body
    '''

def p_subprogram(p):
    '''subprogram : FUNCTION ID decl_param IS decl body
                  | FUNCTION ID decl_param IS body
    '''

def p_body(p):
    ''' body : BEGIN cmd_loop END ID SEMICOLON
    '''

def p_decl(p):
    ''' decl : var SEMICOLON decl
             | var SEMICOLON
		     | subprogram decl
             | subprogram
    ''' 

def p_var(p):
    ''' var : ID COMMA TYPE ASSIGN value
			| ID COLON TYPE
			| var_loop ID COLON TYPE
			| array
    '''

def p_var_loop(p):
    ''' var_loop : var_loop ID COMMA
               | ID COMMA
    '''

def p_decl_param(p):
    ''' decl_param : LPAREN param RPAREN
                  | LPAREN param RPAREN RETURN TYPE
    '''

def p_param(p):
    ''' param : ID COLON TYPE SEMICOLON param
                | ID COLON TYPE SEMICOLON
    '''

def p_function_call(p):
    ''' function_call : ID LPAREN param_pass RPAREN SEMICOLON
    '''

def p_function_call_exp(p):
    ''' function_call_exp : ID LPAREN param_pass RPAREN
    '''

def p_param_pass(p):
    ''' param_pass : expression COMMA param_pass
                   | expression
    '''

def p_value(p):
    ''' value : NUMBER_INT
             | NUMBER_FLOAT
             | NUMBER_EXPONENT
             | BOOLEAN
             | STRING
             | CHAR
    '''

def p_cmd(p):
    ''' cmd : if_statement
			| repeat_statement
			| puts
			| return
			| assign
			| function_call
    '''

def p_cmd_loop(p):
    '''cmd_loop : cmd_loop cmd
                | cmd
    '''

def p_puts(p):
    ''' puts : PUTS LPAREN STRING RPAREN SEMICOLON
    '''

def p_if_statement(p):
    ''' if_statement : IF expression THEN cmd_loop if_statement_loop
    '''

def p_if_statement_loop(p):
    ''' if_statement_loop : ELSIF expression cmd_loop if_statement_loop
                          | ELSE expression cmd_loop END IF SEMICOLON
                          | END IF SEMICOLON
    '''

def p_repeat_statement(p):
    ''' repeat_statement : loop_statement
                         | for_statement
                         | while_statement
    '''

def p_loop_statement(p):
    ''' loop_statement : LOOP cmd_loop END LOOP
    '''

def p_while_statement(p):
    ''' while_statement : WHILE expression NUMBER_INT LOOP cmd_loop END LOOP SEMICOLON
    '''

def p_for_statement(p):
    ''' for_statement : FOR ID IN range LOOP cmd_loop END LOOP SEMICOLON
    '''

def p_range(p):
    ''' range : ID DOTDOT ID
    '''

def p_assign(p):
    ''' assign : ID ASSIGN op_arithmetic SEMICOLON
    '''

def p_expression(p):
    ''' expression : expression AND or_exp
                   | or_exp
    '''

def p_or_exp(p):
    ''' or_exp : or_exp OR comp_exp
               | comp_exp
    '''

def p_comp_exp(p):
    ''' comp_exp : comp_exp comp_op op_arithmetic
                 | op_arithmetic
    '''

def p_comp_op(p):
    ''' comp_op : GREATERTHAN
                | GREATERTHANEQUAL
                | LESSTHAN
                | LESSTHANEQUAL
                | NOTEQUAL
                | EQUAL
    '''

def p_op_arithmetic(p):
    ''' op_arithmetic : op_arithmetic PLUS factor
                      | op_arithmetic MINUS factor
                      | factor
    '''

def p_factor(p):
    ''' factor : factor TIMES power
               | factor DIVIDE power
               | power
    '''

def p_power(p):
    ''' power : power POWER unary
              | unary
    '''

def p_unary(p):
    ''' unary : PLUS term
              | MINUS term 
              | term 
    '''

def p_term(p):
    ''' term : ID
             | function_call_exp
             | LPAREN expression RPAREN
    '''

def p_array(p):
    ''' array : TYPE ID IS ARRAY LPAREN range RPAREN OF TYPE SEMICOLON
    '''

def p_return(p):
    ''' return : RETURN expression SEMICOLON
    '''

# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()

parser.parse(debug=False)