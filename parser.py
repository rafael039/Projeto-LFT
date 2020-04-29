import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
import visitor as vis

def p_subprogram_body(p):
    ''' subprogram_body: subprogram_specification
        IS
        declarative_part
        BEGIN
        sequence_of_statements
        END
        designator
        SEMICOLON
        | subprogram_specification
        IS
        declarative_part
        BEGIN
        sequence_of_statements
        END
        SEMICOLON
    '''
    if len(p) == 9:
        p[0] = ga.c_subprogram_body(p[1],p[3],p[5],p[7])
    else:
        p[0] = ga.c_subprogram_body(p[1],p[3],p[5],None)

def p_designator(p):
    ''' designator: 
        name DOT identifier 
        | name DOT operator_symbol 
        | identifier 
        | operator_symbol
    ''' 
    if len(p) == 4:
        if isinstance(p[3], a_identifier): #dúvida: essa classe identifier é um token? 
            p[0] = ga.c_designator_name_identfier(p[1],p[3])
        else:
            p[0] = ga.c_designator_name_operator_symbol(p[1],p[3])
    else:
        if isinstance(p[3], a_identifier):
            p[0] = ga.c_designator_identfier(p[1])
        else:
            p[0] = ga.c_designator_operator_symbol(p[1])

def p_subprogram_specification(p):
    ''' subprogram_specification:
    PROCEDURE defining_program_unit_name
    '''
    p[0] = ga.c_subprogram_specification(p[2])

def p_declarative_part(p):
    # ocorrência de chaves = recursão
    ''' declarative_part: 
        basic_declarative_item 
        | subprogram_body 
        | basic_declarative_item declarative_part 
        | subprogram_body declarative part
    '''
    if len(p) == 2:
        if isinstance(p[1], a_basic_declarative_item):
            p[0] = ga.c_declarative_part_basic_declarative_item(p[1])
        else:
            p[0] = ga.c_declarative_part_subprogram_body(p[1])
    else: 
        if isinstance(p[1], a_basic_declarative_item):
            p[0] = ga.c_declarative_part_basic_declarative_item_loop(p[1],p[2])
        else: 
            p[0] = ga.c_declarative_part_subprogram_body_loop(p[1],p[2])

def p_basic_declarative_item(p):
    ''' basic_declarative_item: 
    basic_declaration 
    | representation_clause 
    | use_clause 
    '''

    if isinstance(p[1], a_basic_declaration):
        p[0] = ga.c_basic_declarative_item_basic_declaration(p[1])
    elif isinstance(p[1], a_representation_clause):
        p[0] = ga.c_basic_declarative_item_representation_clause(p[1])
    else:
        p[0] = ga.c_basic_declarative_item_use_clause(p[1])


def p_representation_clause(p):
    ''' representation_clause: 
    attribute_definition_clause 
    | enumeration_represation_clause '''

    if isinstance(p[1], a_attribute_definition_clause):
        p[0] = ga.c_representation_clause_attribute_definition_clause(p[1])
    else:
        p[0] = ga.c_representation_clause_enumeration_representation_clause(p[1])

def p_direct_name(p):
    ''' direct_name: 
    identifier 
    | operator_symbol '''

    if isinstance(p[1], a_identifier):
        p[0] = ga.c_direct_name_identifier(p[1])
    else:
        p[0] = ga.c_direct_name_operator_symbol(p[1])
    

def p_attribute_definition_clause(p):
    ''' attribute_definition_name: 
    FOR name SINGLEQUOTE attribute_designator USE expression SEMICOLON 
    | FOR name SINGLEQUOTE attribute designator USE name SEMICOLON '''

    if isinstance(p[6],a_expression):
        p[0] = ga.c_attribute_definition_clause_expression(p[2],p[4],p[6])
    else: 
        p[0] = ga.c_attribute_definition_clause_name(p[2],p[4],p[6])


def p_indexed_component(p):
    ''' indexed_component: 
    name LPAREN expression RPAREN
    | name LPAREN expression COLON indexed_component RPAREN
    '''

    if len(p[0]) == 5:
        p[0] = ga.c_indexed_component(p[1],p[3])
    else:
        p[0] = ga.c_indexed_component_loop(p[1],p[3],p[5])

def p_type_conversion(p):
    '''type_conversion: 
    name LPAREN expression RPAREN
    | name LPAREN name RPAREN ''' 
    
    if isinstance(p[3],a_expression):
        p[0] = ga.c_type_conversion_expression(p[1],p[3])
    else: 
        p[0] = ga.c_type_conversion_name(p[1],p[3])
        
#########################
def p_selected_component(p):
    ''' select_component: 
    name DOT selector_name 
    '''
    p[0] = ga.c_selected_component(p[1],p[3])

def p_attribute_designator(p):
    ''' attribute_designator:
    identifier
    | identifier LPAREN expression RPAREN'''
    if len(p[0]) == 2:
        p[0] = ga.c_attribute_designator_identifier(p[1])
    else:
        p[0] = ga.c_attribute_designator_identifier_expression(p[1],p[3])

def p_expression(p):
    ''' expression: 
    relation AND relation 
    | relation AND relation expression
    | relation AND THEN relation 
    | relation AND THEN relation expression
    | relation OR relation
    | relation OR relation expression
    | relation OR ELSE relation 
    | relation OR ELSE relation expression 
    | relation XOR relation 
    | relation XOR relation expression 
    '''

    if p[2] == 'and': #o valor do lexema AND é o mesmo do t.value, definido no calclex.py
        if p[3] != 'then':
            if len(p[0]) == 4:
                p[0] = ga.c_expression_and(p[1],p[3])
            else:
                p[0] = ga.c_expression_and_loop(p[1],p[3],p[4])
        else:
            if len(p[0]) == 5:
                p[0] = ga.c_expression_and_then(p[1],p[4])
            else:
                p[0] = ga.c_expression_and_then_loop(p[1],p[4],p[5])
    elif p[2] == 'or':
        if p[3] != 'else':
            if len(p[0]) == 4:
                p[0] = ga.c_expression_or(p[1],p[3])
            else:
                p[0] = ga.c_expression_or_loop(p[1],p[3],p[4])
        else:
            if len(p[0]) == 5:
                p[0] = ga.c_expression_or_else(p[1],p[4])
            else:
                p[0] = ga.c_expression_or_else_loop(p[1],p[4],p[5])
    else:
        if len(p[0]) == 4:
            p[0] = ga.c_expression_xor(p[1],p[3])
        else:
            p[0] = ga.c_expression_xor_loop(p[1],p[3],p[4])
        

def p_relation(p):
    ''' relation: 
    simple_expression 
    | simple_expression EQUAL simple_expression 
    | simple_expression NOTEQUAL simple_expression
    | simple_expression LESSTHAN simple_expression
    | simple_expression LESSTHANEQUAL simple_expression
    | simple_expression GREATERTHAN simple_expression
    | simple_expression GREATERTHANEQUAL simple_expression
    | simple_expression IN range 
    | simple_expression IN name
    | simple_expression NOT IN range 
    | simple_expression NOT IN name
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_relation(p[1])
    elif len(p[0]) == 4:
        if p[2] == '=':
            p[0] = ga.c_relation_equal(p[1],p[3])
        elif p[2] == '/=':
            p[0] = ga.c_relation_not_equal(p[1],p[3])
        elif p[2] == '<':
            p[0] = ga.c_relation_less_than(p[1],p[3])
        elif p[2] == '<=':
            p[0] = ga.c_relation_less_than_equal(p[1],p[3])
        elif p[2] == '>':
            p[0] = ga.c_relation_greater_than(p[1],p[3])
        elif p[2] == '>=':
            p[0] = ga.c_relation_greater_than_equal(p[1],p[3])
        else:
            if isinstance(p[3], a_range):
                p[0] = ga.c_relation_in_range(p[1],p[3])
            else:
                p[0] = ga.c_relation_in_name(p[1],p[3])
    else:
        if isinstance(p[4], a_range):
            p[0] = ga.c_relation_not_in_range(p[1],p[3])
        else:
            p[0] = ga.c_relation_not_in_name(p[1],p[3])

def p_simple_expression(p):
    ''' simple_expression:
      term PLUS term 
    | term MINUS term 
    | term CONCAT term 
    | PLUS term PLUS term 
    | PLUS term MINUS term 
    | PLUS term CONCAT term 
    | MINUS term PLUS term 
    | MINUS term MINUS term 
    | MINUS term CONCAT term 
    | term PLUS term simple_expression 
    | term MINUS term simple_expression
    | term CONCAT term simple_expression
    | PLUS term PLUS term simple_expression
    | PLUS term MINUS term simple_expression
    | PLUS term CONCAT term simple_expression
    | MINUS term PLUS term simple_expression
    | MINUS term MINUS term simple_expression
    | MINUS term CONCAT term simple_expression
    '''
    if len(p[0]) == 4:
        if p[2] == '+':
            ga.c_simple_expression_plus(p[1],p[3])
        elif p[2] == '-':
            ga.c_simple_expression_minus(p[1],p[3])
        else:
            ga.c_simple_expression_concat(p[1],p[3])
    elif len(p[0]) == 5:
        if isinstance(p[4], a_term): #dúvida: esse tipo em type precisa ser exatamente o nome da classe? (cogitar testar a classe abstrata ao invés da concreta)
            if p[2] == '+':
                if p[3] == '+':
                    ga.c_simple_expression_plus_plus(p[2],p[4])
                elif p[3] == '-':
                    ga.c_simple_expression_plus_minus(p[2],p[4])
                elif p[3] == '&':
                    ga.c_simple_expression_plus_concat(p[2],p[4])
            else:
                if p[3] == '+':
                    ga.c_simple_expression_minus_plus(p[2],p[4])
                elif p[3] == '-':
                    ga.c_simple_expression_minus_minus(p[2],p[4])
                elif p[3] == '&':
                    ga.c_simple_expression_minus_concat(p[2],p[4])
        else:
            if p[2] == '+':
                ga.c_simple_expression_plus_loop(p[1],p[3],p[4])
            elif p[2] == '-':
                ga.c_simple_expression_minus_loop(p[1],p[3],p[4])
            elif p[2] == '&':
                ga.c_simple_expression_concat_loop(p[1],p[3],p[4])
    else:        
        if p[1] == '+':
            if p[3] == '+':
                ga.c_simple_expression_plus_plus_loop(p[2],p[4],p[5])
            elif p[3] == '-':
                ga.c_simple_expression_plus_minus_loop(p[2],p[4],p[5])
            elif p[3] == '&':
                ga.c_simple_expression_plus_concat_loop(p[2],p[4],p[5])
        else:
            if p[3] == '+':
                ga.c_simple_expression_minus_plus_loop(p[2],p[4],p[5])
            elif p[3] == '-':
                ga.c_simple_expression_minus_minus_loop(p[2],p[4],p[5])
            elif p[3] == '&':
                ga.c_simple_expression_minus_concat_loop(p[2],p[4],p[5])

def p_term(p): 
    ''' term:
    factor
    | factor TIMES factor term
    | factor DIVIDE factor term
    | factor MOD factor term
    | factor REM factor term 
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_term(p[1])
    else:
        if p[2] == '*':
            p[0] = ga.c_term_times(p[1],p[3],p[4])
        elif p[2] == '/':
            p[0] = ga.c_term_divide(p[1],p[3],p[4])
        elif p[2] == 'mod':
            p[0] = ga.c_term_mod(p[1],p[3],p[4])
        else:
            p[0] = ga.c_term_rem(p[1],p[3],p[4])

def p_factor(p):
    ''' factor:
    primary
    | primary POWER primary 
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_factor(p[1])
    else:
        p[0] = ga.c_factor_power(p[1],p[3])

def p_primary(p):
    ''' primary:
    numeric_literal 
    | NULL 
    | string_literal 
    | named_array_aggregate
    | name 
    | qualified_expression 
    | LPAREN expression RPAREN 
    ''' 
    if isinstance(p[1], a_numeric_literal):
        p[0] = ga.c_primary_numeric_literal(p[1])
    elif isinstance(p[1], c_string_literal):
        p[0] = ga.c_primary_string_literal(p[1])
    elif isinstance(p[1], a_named_array_aggregate):
        p[0] = ga.c_primary_named_array_aggregate
    elif isinstance(p[1], a_name):
        p[0] == ga.c_primary_name
    elif p[1] == '(':
        p[0] == ga.c_primary_expression
    else:
        p[0] == ga.c_primary_null

def p_qualified_expression(p):
    ''' qualified_expression: 
    name SINGLE_QUOTE LPAREN expression RPAREN
    | name SINGLE_QUOTE named_array_aggregate
    '''
    if isinstance(p[3], a_expression):
        p[0] = ga.c_qualified_expression_expression(p[1])
    else:
        p[0] = ga.c_qualified_expression_named_array_aggregate(p[1])

def p_named_array_aggregate(p):
    ''' named_array_aggregate: 
    LPAREN array_component_association COMMA array_component_association named_array_aggregate RPAREN 
    |  COMMA array_component_association 
    '''
#371 - Utilizei uma forma diferente para gerar a repetição. Pode gerar algum problema futuro.
    if p[1] == '(':
        p[0] = ga.c_named_array_aggregate_loop(p[2],p[4],p[5])
    else:
        p[0] = ga.c_named_array_aggregate(p[2])

def p_array_component_association(p):
    ''' array_component_association:
    discrete_choice REFASSIGN expression '''
    p[0] = ga.c_array_component_association(p[1],p[3])

def p_discrete_choice_list(p):
    ''' discrete_choice_list: 
    discrete_choice
    | discrete_choice PIPE discrete_choice p_discrete_choice_list
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_discrete_choice_list(p[1])
    else:
        p[0] = ga.c_discrete_choice_list_loop(p[1],p[3],p[4])

def p_discrete_choice(p):
    ''' discrete_choice: 
    expression 
    | discrete_range
    '''
    if isinstance(p[1], a_expression):
        p[0] = ga.c_discrete_choice_expression(p[1])
    else:
        p[0] = ga.c_discrete_choice_discrete_range(p[1])

def p_discrete_range(p):
    '''discrete_range:
    subtype_indication 
    | range
    '''
    if isinstance(p[1], a_subtype_indicator):
        p[0] = ga.c_discrete_range_subtype_indicator(p[1])
    else:
        p[0] = ga.c_discrete_range_range(p[1])

def p_subtype_indication(p):
    ''' subtype_indication: 
    name
    | name constraint
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_subtype_indicator_name(p[1])
    else:
        p[0] = ga.c_subtype_indicator_name_constraint(p[1],p[2]):

def p_constraint(p):
    ''' constraint: 
    range_constraint 
    | digits_constraint 
    | index_constraint 
    | discriminant_constraint 
    '''
    if isinstance(p[1], a_range_constraint):
        p[0] = ga.c_constraint_range_constraint(p[1])
    elif isinstance(p[1], a_digits_constraint):
        p[0] = ga.c_constraint_digits_constraint(p[1])
    elif isinstance(p[1], a_index_constraint):
        p[0] = ga.c_constraint_index_constraint(p[1])
    else:
        p[0] = ga.c_constraint_discriminant_constraint(p[1])
        
def p_discriminant_constraint(p):
    ''' discrimination_constraint:  "(" discriminant_association { "," discriminant_association } ")" '''

def p_discriminant_association(p):
    ''' discriminant_association: [selector_name { "|" selector_name } "=>" ] expression '''

def p_index_constraint(p):
    ''' "(" discrete_range: { "," discrete_range } ")" '''

def p_digits_constraint(p):
    ''' digits_constraint: "digits"  expression [range_constraint] '''

def p_range_constraint(p):
    '''"range: "range" range'''

def p_range(p):
    '''range: (simple_expression ".." simple_expression )'''

def p_range_attribute_reference(p):
    ''' range_attribute_reference: name "'" range_attribute_designator '''

def p_range_attribute_designator(p):
    ''' range_attribute_designator: "Range" ["(" expression ")"] '''

def p_name(p):
    ''' name:
    direct_name 
    | slice 
    | selected_component 
    | attribute_reference 
    | type_conversion
    | function_call
    | character_literal
    | indexed_component '''

    if isinstance(p[1], a_direct_name):
        p[0] = ga.c_name_direct_name(p[1])
    elif isinstance(p[1], a_slice):
        p[0] = ga.c_name_slice(p[1])
    elif isinstance(p[1], a_selected_component):
        p[0] = ga.c_name_selected_component(p[1])
    elif isinstance(p[1], a_attribute_reference):
        p[0] = ga.c_name_attribute_reference(p[1])
    elif isinstance(p[1], a_type_conversion):
        p[0] = ga.c_name_type_conversion(p[1])
    elif isinstance(p[1], a_function_call):
        p[0] = ga.c_name_function_call(p[1])
    elif isinstance(p[1], a_character_literal):
        p[0] = ga.c_name_character_literal(p[1])
    else :
        p[0] = ga.c_name_indexed_component(p[1])

def p_slice(p):
    ''' slice: name "(" discrete_range ")" '''

def p_function_call(p):
    ''' function_call: ( name ) [ actual_parameter_part ] '''

def p_actual_parameter_part(p):
    ''' actual_parameter_part: "(" parameter_association { "," parameter_association } ")" '''

def p_parameter_association(p):
    ''' parameter_association: [ selector_name "=>" ] ( expression | name ) '''

def p_selector_name(p):
    ''' selector_name: identifier | character_literal | operator_symbol '''

def p_character_literal(p):
    ''' character_literal: " ' " graphic_character " ' " '''

def enumeration_represation_clause(p):
    '''enumeration_represation_clause: 'for' direct_name 'use' named_array_aggregate ';' '''

def use_clause(p):
    ''' use_clause: 'use' (name {',' name}) | ('type' name {',' name}) ';' '''

def basic_declaration(p):
    ''' basic_declaration: type_declaratiom | number_declaration | subprogram_declaration '''

def subprogram_declaration(p):
    ''' subprogram_declaration: subprogram_specification ';' '''

def subprogram_specification(p):
    ''' ( 'procedure' defining_program_unit_name ) | ( 'function' defining_program_unit_name ) '''

def defining_program_unit_name(p):
    ''' [ name '.' ] identifier '''

def p_identifier_list(p):
    ''' identifier_list: {"," identifier }'''
    
def p_loop_statement(p):
    '''loop_statement: [name] | [('while' expression)] | ( 'for' identifier 'in'
    ['reverse'] discrete_subtype_definition)] 'loop' sequence_of_statements 'end' 'loop' [name] ';' '''
    
def p_if_statement(p):
    '''if_statement:
     if expression 'then' sequence_of_statements 
     { 'elsif' | expression 'then' sequence_of_statements }
    ['else' sequence_of_statements] 'end' 'if' ';' '''
    
def p_sequence_of_statements(p):
    ''' sequence_of_statements: statement {statement}'''

def p_statement(p):
    '''statement: (simple_statement | compound_statement)'''

def p_compound_statement(p):
    '''compound_statement: if_statement | loop_statement'''

def p_discrete_subtype_definition(p):
    '''discrete_subtype_definition: subtype_indication | range'''

def p_simple_statement(p):
    ''' simple_statement: null_statement | assignment_statement | exit_statement | procedure_call_statement
    | return_statement | entry_call_statement | code_statement '''

def p_entry_call_statement(p):
    '''entry_call_statement: name[atual_paramenter_part] ";" '''

def p_code_statement(p):
    '''code_statement: qualified_expression ";" '''

def p_exit_statement(p):
    '''exit_statement: "exit" [name] ";" '''

def p_null_statement(p):
    '''null_statement: "null" '''

def p_assignment_statement(p):
    ''' assignment_statement: name ":=" expression ";" '''

# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)