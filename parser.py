import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
import visitor as vis



def p_program(p):
    '''program : PROCEDURE ID IS decl BEGIN cmd END ID SEMICOLON
               | PROCEDURE ID IS BEGIN cmd END ID SEMICOLON
    '''

def p_subprogram(p):
    '''subprogram : FUNCTION ID decl_param IS decl BEGIN cmd END ID SEMICOLON
                  | FUNCTION ID decl_param IS BEGIN cmd END ID SEMICOLON
    '''

def p_decl(p):
    ''' decl : var SEMICOLON decl_loop
		     | subprogram decl_loop
    ''' 

def p_decl_loop(p):
    ''' decl_loop : subprogram decl_loop
                  | subprogram
                  | var SEMICOLON decl_loop
                  | var SEMICOLON
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
    ''' param : ID COLON TYPE n_param
    '''

def p_n_param(p):
    ''' n_param : SEMICOLON ID COLON TYPE n_param
                | SEMICOLON ID COLON TYPE
    '''

def p_function_call(p):
    ''' function_call : ID LPAREN param_pass RPAREN SEMICOLON
    '''

def p_function_call_exp(p):
    ''' function_call_exp : ID LPAREN param_pass RPAREN
    '''

def p_param_pass(p):
    ''' param_pass : expression param_pass_loop
	               | op_arithmetic param_pass_loop
    '''

def p_param_pass_loop(p):
    ''' param_pass_loop : SEMICOLON expression param_pass_loop
	                    | SEMICOLON op_arithmetic param_pass_loop
                        | SEMICOLON expression
                        | SEMICOLON op_arithmetic
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
    '''cmd : cmd cmd_loop
           | cmd
    '''

def p_puts(p):
    ''' puts : PUTS LPAREN STRING RPAREN SEMICOLON
    '''

def p_if_statement(p):
    ''' if_statement : IF expression THEN cmd if_statement_loop
    '''

def p_if_statement_loop(p):
    ''' if_statement_loop : ELSIF expression cmd if_statement_loop
                          | ELSE expression cmd END IF SEMICOLON
                          | END IF SEMICOLON
    '''

def p_repeat_statement(p):
    ''' repeat_statement : loop_statement
                         | for_statement
                         | while_statement
    '''

def p_loop_statement(p):
    ''' loop_statement : LOOP cmd END LOOP
    '''

def p_while_statement(p):
    ''' while_statement : WHILE expression NUMBER_INT LOOP cmd END LOOP SEMICOLON
    '''

def p_for_statement(p):
    ''' for_statement : FOR ID IN range LOOP cmd END LOOP SEMICOLON
    '''

def p_range(p):
    ''' range : ID DOTDOT ID
    '''

def p_assign(p):
    ''' assign : ID ASSIGN op_arithmetic SEMICOLON
    '''

def p_expression(p):
    ''' expression : expression AND or_exp
    '''

def p_or_exp(p):
    ''' or_exp : or_exp OR comp_exp
    '''

def p_comp_exp(p):
    ''' comp_exp : comp_exp comp_op bterm
    '''

def p_bterm(p):
    ''' bterm : ID 
              | function_call_exp
              | LPAREN expression RPAREN
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
    ''' power : power POWER term
    '''


def p_term(p):
    ''' term : LPAREN op_arithmetic RPAREN
             | ID
             | function_call_exp
    '''

def p_array(p):
    ''' array : TYPE ID IS ARRAY LPAREN range RPAREN OF TYPE SEMICOLON
    '''

def p_return(p):
    ''' return : RETURN expression
               | RETURN op_arithmetic
    '''


# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()

parser.parse(debug=True)