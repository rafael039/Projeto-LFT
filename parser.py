import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
from visitor import Visitor

def p_program(p):
    '''program : subprogram
               | subprogram program
    '''
    if len(p) == 3:
        p[0] = ga.c_program__decl(p[1],p[2])
    else:
        p[0] = ga.c_program(p[1])

def p_subprogram(p):
    '''subprogram : FUNCTION ID decl_param IS body
                  | PROCEDURE ID IS decl body
                  | PROCEDURE ID IS body
    '''
    if len(p) == 6:
        if isinstance(p[3],ga.a_decl_param):
            p[0] = ga.c_subprogram(p[2],p[3],p[5])
        else:
            ga.c_subprogram__procedure_decl(p[2], p[4], p[5])
    else:
        ga.c_subprogram__procedure(p[2], p[4])

def p_body(p):
    ''' body : BEGIN cmd_loop END ID SEMICOLON
    '''
    p[0] = ga.c_body(p[2],p[4])

def p_decl(p):
    ''' decl : var SEMICOLON decl
             | var SEMICOLON
    ''' 
    if len(p) == 4:
        p[0] = ga.c_decl__var_decl(p[1],p[3])
    else:
        p[0] = ga.c_decl__var(p[1])

def p_var(p):
    ''' var : ID COLON type ASSIGN term
			| ID COLON type
			| var_loop ID COLON type
			| array
    '''
    if len(p) == 6:
        p[0] = ga.c_var__term(p[1],p[3],p[5])
    elif len(p) == 4:
        p[0] = ga.c_var(p[1],p[3])
    elif len(p) == 5:
        p[0] = ga.c_var__var_loop(p[1],p[2],p[4])
    else:
        p[0] = ga.c_var__array(p[1])

def p_var_loop(p):
    ''' var_loop : var_loop ID COMMA
                 | ID COMMA
    '''
    if len(p) == 4:
        p[0] = ga.c_var_loop__loop(p[1],p[2])
    else:
        p[0] = ga.c_var_loop(p[1])

def p_type(p):
    ''' type : BOOLEAN
             | CHARACTER
             | FLOAT
             | INTEGER
             | STRING
    '''
    if p[1] == 'Boolean':
        p[0] = ga.c_type__bool()
    elif p[1] == 'Character':
        p[0] = ga.c_type__char()
    elif p[1] == 'Float':
        p[0] = ga.c_type__float()
    elif p[1] == 'Integer':
        p[0] = ga.c_type__integer()
    else:
        p[0] = ga.c_type__string()



def p_decl_param(p):
    ''' decl_param : LPAREN param RPAREN
                   | LPAREN param RPAREN RETURN type
    '''
    if len(p) == 4:
        p[0] = ga.c_decl_param(p[2])
    else:
        p[0] = ga.c_decl_param__return(p[2],p[5])

def p_param(p):
    ''' param : ID COLON type SEMICOLON param
              | ID COLON type SEMICOLON
    '''
    if len(p) == 6:
        p[0] = ga.c_param__param(p[1],p[3],p[5])
    else:
        p[0] = ga.c_param(p[1],p[3])

def p_function_call(p):
    ''' function_call : ID param_pass SEMICOLON
                      | ID LPAREN RPAREN SEMICOLON
    '''
    if len(p) == 4:
        p[0] = ga.c_function_call(p[1],p[2])
    else:
        p[0] = ga.c_function_call_empty(p[1])


def p_function_call_exp(p):
    ''' function_call_exp : ID param_pass
                          | ID LPAREN RPAREN
    '''
    if len(p) == 3:
        p[0] = ga.c_function_call_exp(p[1],p[2])
    else:
        p[0] = ga.c_function_call_exp_empty(p[1])

def p_param_pass(p):
    ''' param_pass : expression COMMA param_pass
                   | expression
    '''
    if len(p) == 4:
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
    if len(p) == 3:
        p[0] = ga.c_cmd_loop__loop(p[1],p[2])
    else:
        p[0] = ga.c_cmd_loop(p[1])


def p_puts(p):
    ''' puts : PUTS LPAREN STRING RPAREN SEMICOLON
    '''
    p[0] = ga.c_puts(p[3])

def p_if_statement(p):
    ''' if_statement : IF expression THEN cmd_loop if_statement_loop
    '''
    p[0] = ga.c_if_statement(p[2], p[4], p[5])

def p_if_statement_loop(p):
    ''' if_statement_loop : ELSIF expression cmd_loop if_statement_loop
                          | ELSE cmd_loop END IF SEMICOLON
                          | END IF SEMICOLON
    '''
    if len(p) == 6:
       p[0] = ga.c_if_statement_loop__elsif(p[2],p[3],p[4])
    elif len(p) == 7:
       p[0] = ga.c_if_statement_loop__else(p[2])
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
    ''' loop_statement : LOOP cmd_loop END LOOP SEMICOLON
    '''
    p[0] = ga.c_loop_statement(p[2])

def p_while_statement(p):
    ''' while_statement : WHILE expression LOOP cmd_loop END LOOP SEMICOLON
    '''
    p[0] = ga.c_while_statement(p[2], p[4])

def p_for_statement(p):
    ''' for_statement : FOR ID IN range LOOP cmd_loop END LOOP SEMICOLON
    '''
    p[0] = ga.c_for_statement(p[2], p[4], p[6])

def p_range(p):
    ''' range : ID DOTDOT ID
    '''
    p[0] = ga.c_range(p[1],p[3])

def p_assign(p):
    ''' assign : ID ASSIGN op_arithmetic SEMICOLON
    '''
    p[0] = ga.c_assign(p[3])

def p_expression(p):
    ''' expression : expression AND or_exp
                   | or_exp
    '''
    if len(p) == 4:
        p[0] = ga.c_expression__and(p[1], p[3])
    else:
        p[0] = ga.c_expression(p[1])

def p_or_exp(p):
    ''' or_exp : or_exp OR comp_exp
               | comp_exp
    '''
    if len(p) == 4:
        p[0] = ga.c_or_exp__or(p[1], p[3])
    else:
        p[0] = ga.c_or_exp(p[1])

def p_comp_exp(p):
    ''' comp_exp : comp_exp comp_op op_arithmetic
                 | op_arithmetic
    '''
    if len(p) == 4:
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
        p[0] = ga.c_factor__power(p[1])

def p_power(p):
    ''' power : power POWER unary
              | unary
    '''
    if len(p) == 4:
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
        p[0] = ga.c_unary(p[1])

def p_term(p):
    ''' term : ID
             | function_call_exp
             | LPAREN expression RPAREN
             | literal
    '''
    if len(p) == 3:
        p[0] = ga.c_term__expression(p[2])
    else:
        if isinstance(p[1],ga.a_function_call_exp):
            p[0] = ga.c_term__function_call(p[1])
        elif isinstance(p[1], ga.a_literal):
            p[0] = ga.c_term__literal(p[1])
        else:
            p[0] = ga.c_term__ID(p[1])

def p_literal(p):
    ''' literal : CHAR
                | NUMBER_FLOAT
                | NUMBER_INT
                | STR
                | TRUE
                | FALSE
    '''
    if type(p[1]) == float:
        p[0] = ga.c_literal_float(p[1])
    elif type(p[1]) == int:
        p[0] = ga.c_literal_int(p[1])
    elif type(p[1]) == str:
        p[0] = ga.c_literal_str(p[1])
    elif p[1] == 'True':
        p[0] = ga.c_literal_true(p[1])
    elif p[1] == 'False':
        p[0] = ga.c_literal_false(p[1])
    else:
        p[0] = ga.c_literal_char(p[1])


def p_array(p):
    ''' array : type ID IS ARRAY LPAREN range RPAREN OF type SEMICOLON
    '''
    p[0] = ga.c_array(p[1],p[2],p[6],p[9])

def p_return(p):
    ''' return : RETURN expression SEMICOLON
    '''
    p[0] = ga.c_return(p[2])

# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()
result = parser.parse(debug=True)
visitor = Visitor()
result.accept(visitor)
# semanticVisitor = SemanticVisitor()
# result.accept(semanticVisitor)
