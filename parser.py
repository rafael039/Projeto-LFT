import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
import visitor as vis

def p_program(p):
    '''program : PROCEDURE ID IS decl body
               | PROCEDURE ID IS body
    '''
    if len(p[0]) == 6:
        p[0] = ga.c_program__decl(p[4],p[5])
    else:
        p[0] = ga.c_program(p[4])

def p_subprogram(p):
    '''subprogram : FUNCTION ID decl_param IS decl body
                  | FUNCTION ID decl_param IS body
    '''
    if len(p[0]) == 7:
        p[0] = ga.c_subprogram__decl(p[3],p[5],p[6])
    else:
        p[0] = ga.c_subprogram(p[3],p[5])

def p_body(p):
    ''' body : BEGIN cmd_loop END ID SEMICOLON
    '''
    p[0] = ga.c_body(p[2])

def p_decl(p):
    ''' decl : var SEMICOLON decl
             | var SEMICOLON
		     | subprogram decl
             | subprogram
    ''' 
    if len(p[0]) == 4:
        p[0] = ga.c_decl__var_decl(p[1],p[3])
    elif len(p[0]) == 3:
        if isinstance(p[1], ga.a_var):
            p[0] = ga.c_decl__var(p[1])
        else:
            p[0] = ga.c_decl__subprogram_decl(p[1],p[2])
    else:
        p[0] = ga.c_decl__subprogram(p[1])

def p_var(p):
    ''' var : ID COMMA TYPE ASSIGN ID
			| ID COLON TYPE
			| var_loop ID COLON TYPE
			| array
    '''
    if len(p[0]) == 6:
        p[0] = ga.c_var__ID()
    elif len(p[0]) == 4:
        p[0] = ga.c_var()
    elif len(p[0]) == 5:
        p[0] = ga.c_var__var_loop(p[1])
    else:
        p[0] = ga.c_var__array(p[1])

def p_var_loop(p):
    ''' var_loop : var_loop ID COMMA
                 | ID COMMA
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_var_loop__loop(p[1])
    else:
        p[0] = ga.c_var_loop()

def p_decl_param(p):
    ''' decl_param : LPAREN param RPAREN
                   | LPAREN param RPAREN RETURN TYPE
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_decl_param(p[2])
    else:
        p[0] = ga.c_decl_param__return(p[2])

def p_param(p):
    ''' param : ID COLON TYPE SEMICOLON param
              | ID COLON TYPE SEMICOLON
    '''
    if len(p[0]) == 6:
        p[0] = ga.c_param__param(p[5])
    else:
        p[0] = ga.c_param()

def p_function_call(p):
    ''' function_call : ID LPAREN param_pass RPAREN SEMICOLON
    '''
    p[0] = ga.c_function_call(p[3])

def p_function_call_exp(p):
    ''' function_call_exp : ID LPAREN param_pass RPAREN
    '''
    p[0] = ga.c_function_call_exp(p[3])

def p_param_pass(p):
    ''' param_pass : expression COMMA param_pass
                   | expression
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_param_pass__param_pass(p[1],p[3])
    else:
        p[0] = ga.c_param_pass(p[1])

def p_cmd(p):
    ''' cmd : if_statement
			| repeat_statement
			| puts
			| return
			| assign
			| function_call
    '''
    if isinstance(p[0], ga.a_if_statement):
        p[0] = ga.c_cmd__if_statement(p[1])
    elif isinstance(p[0], ga.a_repeat_statement):
        p[0] = ga.c_cmd__repeat_statement(p[1])
    elif isinstance(p[0], ga.a_puts):
        p[0] = ga.c_cmd__puts(p[1])
    elif isinstance(p[0], ga.a_return):
        p[0] = ga.c_cmd__return(p[1])
    elif isinstance(p[0], ga.a_assign):
        p[0] = ga.c_cmd__assign(p[1])
    else:
        p[0] = ga.c_function_call(p[1])
        
        
def p_cmd_loop(p):
    '''cmd_loop : cmd_loop cmd
                | cmd
    '''
    if len(p[0]) == 3:
        p[0] = ga.c_cmd_loop__loop(p[1],p[2])
    else:
        p[0] = ga.c_cmd_loop(p[1])


def p_puts(p):
    ''' puts : PUTS LPAREN STRING RPAREN SEMICOLON
    '''
    p[0] = ga.c_puts()  

def p_if_statement(p):
    ''' if_statement : IF expression THEN cmd_loop if_statement_loop
    '''
    p[0] = ga.c_if_statement(p[2], p[4], p[5])

def p_if_statement_loop(p):
    ''' if_statement_loop : ELSIF expression cmd_loop if_statement_loop
                          | ELSE expression cmd_loop END IF SEMICOLON
                          | END IF SEMICOLON
    '''
    if len(p[0]) == 6:
       p[0] = ga.c_if_statement_loop__elsif(p[2],p[3],p[4])
    elif len(p[0]) == 7:
       p[0] = ga.c_if_statement_loop__else(p[2],p[3])
    else:
       p[0] = ga.c_if_statement_loop__end()
         
       
def p_repeat_statement(p):
    ''' repeat_statement : loop_statement
                         | for_statement
                         | while_statement
    '''
    if isinstance(p[1], ga.a_loop_statement):
        p[0] = ga.c_repeat_statement__loop(p[1])
    elif isinstance(p[1], ga.a_for_statement):
        p[0] = ga.c_repeat_statement__for(p[1])
    else:
        p[0] = ga.c_repeat_statement__while(p[1])

def p_loop_statement(p):
    ''' loop_statement : LOOP cmd_loop END LOOP
    '''
    p[0] = ga.c_loop_statement(p[2])

def p_while_statement(p):
    ''' while_statement : WHILE expression NUMBER_INT LOOP cmd_loop END LOOP SEMICOLON
    '''
    p[0] = ga.c_while_statement(p[2], p[5])

def p_for_statement(p):
    ''' for_statement : FOR ID IN range LOOP cmd_loop END LOOP SEMICOLON
    '''
    p[0] = ga.c_for_statement(p[4], p[6])

def p_range(p):
    ''' range : ID DOTDOT ID
    '''
    p[0] = ga.c_range()

def p_assign(p):
    ''' assign : ID ASSIGN op_arithmetic SEMICOLON
    '''
    p[0] = ga.c_assign(p[3])

def p_expression(p):
    ''' expression : expression AND or_exp
                   | or_exp
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_expression__and(p[1], p[3])
    else:
        p[0] = ga.c_expression(p[1])

def p_or_exp(p):
    ''' or_exp : or_exp OR comp_exp
               | comp_exp
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_or_exp__or(p[1], p[3])
    else:
        p[0] = ga.c_or_exp(p[1])

def p_comp_exp(p):
    ''' comp_exp : comp_exp comp_op op_arithmetic
                 | op_arithmetic
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_comp_exp__op_arithmetic(p[1], p[2], p[3])
    else:
        p[0] = ga.c_comp_exp(p[1])

def p_comp_op(p):
    ''' comp_op : GREATERTHAN
                | GREATERTHANEQUAL
                | LESSTHAN
                | LESSTHANEQUAL
                | NOTEQUAL
                | EQUAL 
    '''
    if p[1] == '>':
        p[0] = ga.c_comp_op__GT()
    elif p[1] == '>=':
        p[0] = ga.c_comp_op__GTE()
    elif p[1] == '<':
        p[0] = ga.c_comp_op__LT()
    elif p[1] == '<=':
        p[0] = ga.c_comp_op__LTE()
    elif p[1] == '/=':
        p[0] = ga.c_comp_op__NE()
    else:
        p[0] = ga.c_comp_op__E()

def p_op_arithmetic(p):
    ''' op_arithmetic : op_arithmetic PLUS factor
                      | op_arithmetic MINUS factor
                      | factor
    '''
    if p[2] == '+':
        p[0] = ga.c_op_arithmetic__PLUS(p[1], p[3])
    elif p[2] == '-':
        p[0] = ga.c_op_arithmetic__MINUS(p[1], p[3])
    else: 
        p[0] = ga.c_op_arithmetic__factor(p[1])

def p_factor(p):
    ''' factor : factor TIMES power
               | factor DIVIDE power
               | power
    '''
    if p[2] == '*':
        p[0] = ga.c_factor__TIMES(p[1], p[3])
    elif p[2] == '/':
        p[0] = ga.c_factor__DIVIDE(p[1], p[3])
    else:
        p[0] = ga.c_factor__power

def p_power(p):
    ''' power : power POWER unary
              | unary
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_power(p[1], p[3])
    else:
        p[0] = ga.c_power__unary(p[1])

def p_unary(p):
    ''' unary : PLUS term
              | MINUS term 
              | term 
    '''
    if p[1] == '+':
        p[0] = ga.c_unary__PLUS(p[2])
    elif p[1] == '-':
        p[0] = ga.c_unary__MINUS(p[2])
    else:
        p[0] = ga.c_unary

def p_term(p):
    ''' term : ID
             | function_call_exp
             | LPAREN expression RPAREN
    '''
    if len(p[0]) == 3:
        p[0] = ga.c_term__expression(p[2])
    elif len(p[0]) == 1:
        p[0] = ga.c_term__function_call(p[1])
    else:
        p[0] = ga.c_term__ID()        

def p_array(p):
    ''' array : TYPE ID IS ARRAY LPAREN range RPAREN OF TYPE SEMICOLON
    '''
    p[0] = ga.c_array(p[6])

def p_return(p):
    ''' return : RETURN expression SEMICOLON
    '''
    p[0] = ga.c_return(p[2])

# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()

parser.parse(debug=False)