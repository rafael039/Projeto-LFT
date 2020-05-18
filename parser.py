import ply.yacc as yacc
from calclex import tokens
import gramAbstrata as ga
import visitor as vis

def p_subprogram_body(p):
    '''subprogram_body : subprogram_specification IS declarative_part BEGIN sequence_of_statements END designator SEMICOLON
        | subprogram_specification IS declarative_part BEGIN sequence_of_statements END SEMICOLON
    '''
    if len(p) == 9:
        p[0] = ga.c_subprogram_body(p[1],p[3],p[5],p[7])
    else:
        p[0] = ga.c_subprogram_body(p[1],p[3],p[5],None)


def p_designator(p):
    ''' designator : name DOT ID
        | ID
    ''' 
    if len(p) == 4:
        p[0] = ga.c_designator_name_identfier(p[1],p[3])

    else:
        p[0] = ga.c_designator_identfier(p[1])

def p_subprogram_specification(p):
    ''' subprogram_specification : PROCEDURE defining_program_unit_name
    '''
    p[0] = ga.c_subprogram_specification(p[2])

def p_declarative_part(p):
    # ocorrência de chaves = recursão
    ''' declarative_part : basic_declarative_item
        | subprogram_body 
        | basic_declarative_item declarative_part 
        | subprogram_body declarative_part
    '''
    if len(p) == 2:
        if isinstance(p[1], ga.a_basic_declarative_item):
            p[0] = ga.c_declarative_part_basic_declarative_item(p[1])
        else:
            p[0] = ga.c_declarative_part_subprogram_body(p[1])
    else: 
        if isinstance(p[1], ga.a_basic_declarative_item):
            p[0] = ga.c_declarative_part_basic_declarative_item_loop(p[1],p[2])
        else: 
            p[0] = ga.c_declarative_part_subprogram_body_loop(p[1],p[2])

def p_basic_declarative_item(p):
    ''' basic_declarative_item : basic_declaration
    | representation_clause 
    | use_clause 
    '''
    
    if isinstance(p[1], ga.a_basic_declarative_item):
        p[0] = ga.c_basic_declarative_item_basic_declaration(p[1])
    elif isinstance(p[1], ga.a_representation_clause):
        p[0] = ga.c_basic_declarative_item_representation_clause(p[1])
    else:
        p[0] = ga.c_basic_declarative_item_use_clause(p[1])


def p_representation_clause(p):
    ''' representation_clause : attribute_definition_clause
    | enumeration_representation_clause '''

    if isinstance(p[1], ga.a_attribute_definition_clause):
        p[0] = ga.c_representation_clause_attribute_definition_clause(p[1])
    else:
        p[0] = ga.c_representation_clause_enumeration_representation_clause(p[1])

def p_direct_name(p):
    ''' direct_name : ID'''
    p[0] = ga.c_direct_name_identifier(p[1])
    

def p_attribute_definition_clause(p):
    ''' attribute_definition_clause : FOR name SINGLEQUOTE attribute_designator USE expression SEMICOLON
    | FOR name SINGLEQUOTE attribute_designator USE name SEMICOLON '''

    if isinstance(p[6], ga.a_expression):
        p[0] = ga.c_attribute_definition_clause_expression(p[2],p[4],p[6])
    else: 
        p[0] = ga.c_attribute_definition_clause_name(p[2],p[4],p[6])


def p_indexed_component(p):
    ''' indexed_component : name LPAREN expression RPAREN
    | name LPAREN expression COLON indexed_component RPAREN
    '''

    if len(p[0]) == 5:
        p[0] = ga.c_indexed_component(p[1],p[3])
    else:
        p[0] = ga.c_indexed_component_loop(p[1],p[3],p[5])

def p_type_conversion(p):
    '''type_conversion : name LPAREN expression RPAREN
    | name LPAREN name RPAREN ''' 
    
    if isinstance(p[3], ga.a_expression):
        p[0] = ga.c_type_conversion_expression(p[1],p[3])
    else: 
        p[0] = ga.c_type_conversion_name(p[1],p[3])
        
def p_selected_component(p):
    ''' selected_component : name DOT selector_name
    '''
    p[0] = ga.c_selected_component(p[1],p[3])

def p_attribute_reference(p):
    ''' attribute_reference : name SINGLEQUOTE attribute_designator
    '''
    p[0] = ga.c_attribute_reference(p[1],p[3])

def p_attribute_designator(p):
    ''' attribute_designator : ID
    | ID LPAREN expression RPAREN'''
    if len(p[0]) == 2:
        p[0] = ga.c_attribute_designator_identifier(p[1])
    else:
        p[0] = ga.c_attribute_designator_identifier_expression(p[1],p[3])

def p_expression(p):
    ''' expression : relation AND relation
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
    ''' relation : simple_expression
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
            if isinstance(p[3], ga.a_range):
                p[0] = ga.c_relation_in_range(p[1],p[3])
            else:
                p[0] = ga.c_relation_in_name(p[1],p[3])
    else:
        if isinstance(p[4], ga.a_range):
            p[0] = ga.c_relation_not_in_range(p[1],p[3])
        else:
            p[0] = ga.c_relation_not_in_name(p[1],p[3])

def p_simple_expression(p):
    ''' simple_expression : simple_expression PLUS term
    | simple_expression MINUS term
    | simple_expression CONCAT term
    | unaryExp
    '''
    #if p[2] == '+':
    if len(p[0]) == 4:
        if p[2] == '+':
            ga.c_simple_expression_plus(p[1],p[3])
        elif p[2] == '-':
            ga.c_simple_expression_minus(p[1],p[3])
        else:
            ga.c_simple_expression_concat(p[1],p[3])
    elif len(p[0]) == 5:
        if isinstance(p[4], ga.a_term): #dúvida: esse tipo em type precisa ser exatamente o nome da classe? (cogitar testar a classe abstrata ao invés da concreta)
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

def p_unary_exp(p):
    '''unaryExp : PLUS term
              | MINUS term
              | term
              '''
    pass

def p_term(p): 
    ''' term : factor
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
    ''' factor : primary
    | primary POWER primary 
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_factor(p[1])
    else:
        p[0] = ga.c_factor_power(p[1],p[3])

def p_numeric_literal(p): #
    '''numeric_literal : NUMBER_INT
    | NUMBER_FLOAT
    | NUMBER_EXPONENT
    '''

def p_primary(p):
    ''' primary : numeric_literal
    | NULL  
    | named_array_aggregate
    | name 
    | qualified_expression 
    | LPAREN expression RPAREN 
    ''' 
    if isinstance(p[1], ga.a_numeric_literal):
        p[0] = ga.c_primary_numeric_literal(p[1])
    elif isinstance(p[1], ga.a_string_literal):
        p[0] = ga.c_primary_string_literal(p[1])
    elif isinstance(p[1], ga.a_named_array_aggregate):
        p[0] = ga.c_primary_named_array_aggregate
    elif isinstance(p[1], ga.a_name):
        p[0] == ga.c_primary_name
    elif p[1] == '(':
        p[0] == ga.c_primary_expression
    else:
        p[0] == ga.c_primary_null

def p_qualified_expression(p):
    ''' qualified_expression : name SINGLEQUOTE LPAREN expression RPAREN
    | name SINGLEQUOTE named_array_aggregate
    '''
    if isinstance(p[3], ga.a_expression):
        p[0] = ga.c_qualified_expression_expression(p[1])
    else:
        p[0] = ga.c_qualified_expression_named_array_aggregate(p[1])

def p_named_array_aggregate(p):
    ''' named_array_aggregate : LPAREN array_component_association COMMA array_component_association named_array_aggregate RPAREN
    |  COMMA array_component_association 
    '''
#371 - Utilizei uma forma diferente para gerar a repetição. Pode gerar algum problema futuro.
    if p[1] == '(':
        p[0] = ga.c_named_array_aggregate_loop(p[2],p[4],p[5])
    else:
        p[0] = ga.c_named_array_aggregate(p[2])

def p_array_component_association(p):
    ''' array_component_association : discrete_choice_list REFASSIGN expression '''
    p[0] = ga.c_array_component_association(p[1],p[3])

def p_discrete_choice_list(p):
    ''' discrete_choice_list : discrete_choice
    | discrete_choice PIPE discrete_choice discrete_choice_list
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_discrete_choice_list(p[1])
    else:
        p[0] = ga.c_discrete_choice_list_loop(p[1],p[3],p[4])

def p_discrete_choice(p):
    ''' discrete_choice : expression
    | discrete_range
    '''
    if isinstance(p[1], ga.a_expression):
        p[0] = ga.c_discrete_choice_expression(p[1])
    else:
        p[0] = ga.c_discrete_choice_discrete_range(p[1])

def p_discrete_range(p):
    '''discrete_range : subtype_indication
    | range
    '''
    if isinstance(p[1], ga.a_subtype_indicator):
        p[0] = ga.c_discrete_range_subtype_indicator(p[1])
    else:
        p[0] = ga.c_discrete_range_range(p[1])

def p_subtype_indication(p):
    ''' subtype_indication : name
    | name constraint
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_subtype_indicator_name(p[1])
    else:
        p[0] = ga.c_subtype_indicator_name_constraint(p[1],p[2])

def p_constraint(p):
    ''' constraint : range_constraint
    | digits_constraint 
    | index_constraint 
    | discriminant_constraint 
    '''
    if isinstance(p[1], ga.a_range_constraint):
        p[0] = ga.c_constraint_range_constraint(p[1])
    elif isinstance(p[1], ga.a_digits_constraint):
        p[0] = ga.c_constraint_digits_constraint(p[1])
    elif isinstance(p[1], ga.a_index_constraint):
        p[0] = ga.c_constraint_index_constraint(p[1])
    else:
        p[0] = ga.c_constraint_discriminant_constraint(p[1])
        
def p_discriminant_constraint(p):
    ''' discriminant_constraint : LPAREN discriminant_association COMMA discriminant_association RPAREN
    | COMMA discriminant_association '''
    
    if p[1] == '(':
        p[0] = ga.c_discriminant_constraint_loop(p[2],p[4],p[5])
    else:
        p[0] = ga.c_discriminant_constraint(p[2])



def p_discriminant_association(p):
    ''' discriminant_association : selector_name PIPE selector_name REFASSIGN expression
    | selector_name PIPE selector_name discriminant_association REFASSIGN expression 
    | PIPE selector_name 
    | expression
    '''
    if len(p[0]) == 6:
        p[0] = ga.c_discriminant_association(p[1],p[3],p[5])  
    elif len(p[0]) == 7: 
        p[0] = ga.c_discriminant_association_loop(p[1],p[3],p[4],p[6])
    elif len(p[0]) == 3:
        p[0] = ga.c_discriminant_association_pipe(p[2])
    elif len(p[0]) == 1:
        p[0] = ga.c_discriminant_association_expression(p[1])


def p_index_constraint(p):
    ''' index_constraint : LPAREN discrete_range RPAREN
    | LPAREN discrete_range COMMA discrete_range index_constraint RPAREN 
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_index_constraint(p[2])
    elif len(p[0]) == 7:
        p[0] = ga.c_index_constraint_loop(p[2],p[4],p[5])

def p_digits_constraint(p):
    ''' digits_constraint : DIGITS expression range_constraint
    | DIGITS expression
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_digits_constraint_range(p[2], p[3])
    else:
        p[0] = ga.c_digits_constraint(p[2])

def p_range_constraint(p):
    '''range_constraint : RANGE range
    '''
    p[0] = ga.c_range_constraint(p[2])

def p_range(p):
    '''range : range_attribute_reference
    | simple_expression DOTDOT simple_expression 
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_range_attribute(p[1])
    elif len(p[0]) == 4:
        p[0] = ga.c_range_simple_expression(p[1],p[3])

def p_range_attribute_reference(p):
    ''' range_attribute_reference : name SINGLEQUOTE range_attribute_designator
    '''
    p[0] = ga.c_range_attribute_reference(p[1], p[3])

def p_range_attribute_designator(p):
    ''' range_attribute_designator : RANGE
    | RANGE LPAREN expression RPAREN 
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_range_attribute_designator()
    else:
        p[0] = ga.c_range_attribute_designator_expression(p[3])

def p_name(p):
    ''' name : direct_name
    | slice 
    | selected_component 
    | attribute_reference 
    | type_conversion
    | function_call
    | character_literal
    | indexed_component '''

    if isinstance(p[1], ga.a_direct_name):
        p[0] = ga.c_name_direct_name(p[1])
    elif isinstance(p[1], ga.a_slice):
        p[0] = ga.c_name_slice(p[1])
    elif isinstance(p[1], ga.a_selected_component):
        p[0] = ga.c_name_selected_component(p[1])
    elif isinstance(p[1], ga.a_attribute_reference):
        p[0] = ga.c_name_attribute_reference(p[1])
    elif isinstance(p[1], ga.a_type_conversion):
        p[0] = ga.c_name_type_conversion(p[1])
    elif isinstance(p[1], ga.a_function_call):
        p[0] = ga.c_name_function_call(p[1])
    elif isinstance(p[1], ga.a_character_literal):
        p[0] = ga.c_name_character_literal(p[1])
    else :
        p[0] = ga.c_name_indexed_component(p[1])

def p_slice(p):
    ''' slice : name LPAREN discrete_range RPAREN
    '''
    p[0] = ga.c_slice(p[1],p[3])

def p_function_call(p):
    ''' function_call : name
    | name actual_parameter_part
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_function_call(p[1])
    else:
        p[0] = ga.c_function_call_actual_parameter_part(p[1],p[2])

def p_actual_parameter_part(p):
    ''' actual_parameter_part : LPAREN parameter_association RPAREN
                                   | LPAREN parameter_association actual_parameter_part_loop RPAREN
    '''
    if len(p[0]) == 5:
        p[0] = ga.c_actual_parameter_part_loop(p[2],p[3])
    elif len(p[0]) == 4:
        p[0] = ga.c_actual_parameter_part_paren(p[2])
    else:
        p[0] = ga.c_actual_parameter_part_comma(p[2])

def p_actual_parameter_part_loop(p): #
    ''' actual_parameter_part_loop : COMMA parameter_association actual_parameter_part_loop
                                   | COMMA parameter_association
    '''

def p_parameter_association(p):
    ''' parameter_association : expression
    | name
    | selector_name REFASSIGN expression
    | selector_name REFASSIGN name 
    '''
    if len(p[0]) == 2:
        if isinstance(p[1], ga.a_expression):
            p[0] = ga.c_parameter_association_expression(p[1])
        else:
            p[0] = ga.c_parameter_association_name(p[1])
    else:
        if isinstance(p[3], ga.a_expression):
            p[0] = ga.c_parameter_association_selector_name_expression(p[1],p[3])
        else: 
            p[0] = ga.c_parameter_association_selector_name_name(p[1],p[3])
        

def p_selector_name(p):
    ''' selector_name : ID
    | character_literal 
    '''
    if isinstance(p[1], ga.a_identifier): 
        p[0] = ga.c_selector_name_identifier(p[1])
    else:
        p[0] = ga.c_selector_name_character_literal(p[1])

def p_graphic_character(p): #
    '''graphic_character : SPACE
    | NUMBER_INT
    | IDENTIFIER_LETTER_UPPER
    | IDENTIFIER_LETTER_LOWER
    '''

def p_character_literal(p):
    ''' character_literal : SINGLEQUOTE graphic_character SINGLEQUOTE
    '''
    p[0] = ga.c_character_literal(p[2])

def p_enumeration_representation_clause(p):
    ''' enumeration_representation_clause : FOR direct_name USE named_array_aggregate SEMICOLON '''
    p[0] = ga.c_enumeration_representation_clause(p[2],p[4])

def p_use_clause(p):
    ''' use_clause : LPAREN USE name RPAREN
    | LPAREN TYPE name RPAREN
    | LPAREN USE name use_clause_loop RPAREN
    | LPAREN TYPE name use_clause_loop RPAREN
    '''
    if len(p[0]) == 4: 
        p[0] = ga.c_use_clause_loop(p[2],p[3])
    elif p[1] == 'use':
        p[0] = ga.c_use_clause_use(p[2])
    else :
        p[0] = ga.c_use_clause_type(p[2])

def p_use_clause_loop(p):
    ''' use_clause_loop : COMMA name use_clause_loop
                        | COMMA name
    '''
    if len(p[0]) == 2 :
        p[0] = ga.c_use_clause_loop(p[2])
    else:
        p[0] = ga.c_use_clause_loop(p[2],p[3])

def p_discriminant_part(p): #
    '''discriminant_part : identifier_list COLON name ASSIGN expression '''
    p[0] = ga.c_discriminant_part(p[1],p[3],p[5])


def p_incomplete_type_definition(p):
    '''
    incomplete_type_definition : TYPE ID SEMICOLON
    | TYPE ID discriminant_part SEMICOLON
    '''
    if len(p[0]) == 4:
        p[0] = ga.c_incomplete_type_definition(p[2])
    else:
        p[0] = ga.c_incomplete_type_definition_discriminant_part(p[2],p[3])

def p_basic_declaration(p):
    ''' basic_declaration : incomplete_type_definition
    | number_declaration 
    | subprogram_declaration
    '''
    if isinstance(p[1], ga.a_incomplete_type_definition):
        p[0] = ga.c_basic_declaration_incomplete_type_definition(p[1])
    elif isinstance(p[1], ga.a_number_declaration):
        p[0] = ga.c_basic_declaration_number_declaration(p[1])
    else:
        p[0] = ga.c_basic_declaration_subprogram_declaration(p[1])


def p_subprogram_declaration(p):
    '''subprogram_declaration : subprogram_specification SEMICOLON
    '''
    p[0] = ga.c_subprogram_declaration(p[1])
    

def p_defining_program_unit_name(p):
    ''' defining_program_unit_name : ID
    | name DOT ID '''

    if isinstance(p[1], ga.a_identifier):
        p[0] = ga.c_defining_program_unit_name_identifier(p[1])
    else:
        p[0] = ga.c_defining_program_unit_name_name_identifier(p[1],p[3])

def p_number_declaration(p):
    ''' number_declaration : COLON CONSTANT ASSIGN expression SEMICOLON
    '''
    p[0] = ga.c_number_declaration(p[4])

def p_identifier_list(p):
    ''' identifier_list : ID
                         | ID COMMA identifier_list
    '''
    # como fazer o loop aqui?

def p_loop_statement(p):
    ''' loop_statement : LOOP sequence_of_statements END LOOP SEMICOLON LOOP sequence_of_statements END LOOP name SEMICOLON
    | LPAREN WHILE expression RPAREN LOOP sequence_of_statements END LOOP SEMICOLON
    | LPAREN WHILE expression RPAREN LOOP sequence_of_statements END LOOP name SEMICOLON
    | LPAREN FOR ID IN discrete_subtype_definition RPAREN LOOP sequence_of_statements END LOOP SEMICOLON
    | LPAREN FOR ID IN discrete_subtype_definition RPAREN LOOP sequence_of_statements END LOOP name SEMICOLON
    | LPAREN FOR ID IN REVERSE discrete_subtype_definition RPAREN LOOP sequence_of_statements END LOOP SEMICOLON
    | LPAREN FOR ID IN REVERSE discrete_subtype_definition RPAREN LOOP sequence_of_statements END LOOP name SEMICOLON
    '''
    if len(p[0]) == 6:
        p[0] = ga.c_loop_statement(p[2])
    elif len(p[0]) == 7:
        p[0] = ga.c_loop_statement_name(p[2],p[5])
    elif len(p[0]) == 8:
        p[0] = ga.c_loop_statement_while(p[3],p[6])
    elif len(p[0]) == 9:
        p[0] = ga.c_loop_statement_while_name(p[3],p[6],p[9])
    elif len(p[0]) == 12:
        p[0] = ga.c_loop_statement_for(p[3],p[5],p[8])
    elif len(p[0]) == 13:
        if isinstance(p[6], ga.a_discrete_subtype_definition):
            p[0] = ga.c_loop_statement_for_name(p[3],p[5],p[8],p[11])
        else:
            p[0] = ga.c_loop_statement_for_reverse(p[3],p[6],p[9])
    else:
        p[0] = ga.c_loop_statement_for_reverse_name(p[3],p[6],p[9],p[12])

def p_if_statement(p):
    '''if_statement : IF expression THEN sequence_of_statements if_statemant_loop
    '''

    if len(p[0]) == 8:
        p[0] = ga.c_if_statement(p[2],p[4])
    elif len(p[0]) == 12:
        p[0] = ga.c_if_statement_elsif(p[2],p[4],p[6],p[8])
    elif len(p[0]) == 13:
        p[0] = ga.c_if_statement_elsif_loop(p[2],p[4],p[6],p[8],p[9])
    else:
        p[0] = ga.c_if_statement_else(p[2],p[4],p[6])

def p_if_statemant_loop(p):
    ''' if_statemant_loop : ELSIF sequence_of_statements if_statemant_loop 
                           | ELSE sequence_of_statements END IF SEMICOLON 
                           | END IF SEMICOLON
    '''

def p_sequence_of_statements(p):
    ''' sequence_of_statements : statement sequence_of_statements
                                | statement
    '''
    if len(2):
        p[0] = ga.c_sequence_of_statements(p[1])
    else:
        p[0] = ga.c_sequence_of_statements_loop(p[1],p[2])

def p_statement(p):
    '''statement : simple_statement
                 | compound_statement
    '''
    if isinstance(p[1], ga.a_simple_statement):
        p[0] = ga.c_statement_simple_statement(p[1])
    else:
        p[0] = ga.c_statement_compound_statement(p[1])

def p_compound_statement(p):
    '''compound_statement : if_statement
                          | loop_statement
    '''
    if isinstance(p[1], ga.a_compound_statement):
        p[0] = ga.c_compound_statement_if_statement(p[1])
    else:
        p[0] = ga.c_compound_statement_loop_statement(p[1])

def p_discrete_subtype_definition(p):
    '''discrete_subtype_definition : subtype_indication
                                    | range
     '''
    if isinstance(p[1],ga.a_subtype_indicator):
        p[0] = ga.c_discrete_subtype_definition_subtype_indication(p[1])
    else:
        p[0] = ga.c_discrete_subtype_definition_range(p[1])

def p_simple_statement(p):
    ''' simple_statement : null_statement
    | assignment_statement
    | exit_statement 
    | entry_call_statement 
    | code_statement 
    '''
    if isinstance(p[1], ga.a_null_statement):
        p[0] = ga.c_simple_statement_null_statement(p[1])
    elif isinstance(p[1], ga.a_assignment_statement):
        p[0] = ga.c_simple_statement_assignment_statement(p[1])
    elif isinstance(p[1],ga.a_exit_statement):
        p[0] = ga.c_simple_statement_exit_statement(p[1])
    else:
        p[0] = ga.c_simple_statement_code_statement(p[1])

def p_entry_call_statement(p):
    '''entry_call_statement : name SEMICOLON
    | name actual_parameter_part SEMICOLON
    '''
    if len(p[0]) == 2:
        p[0] = ga.c_entry_call_statement(p[1])
    else:
        p[0] = ga.c_entry_call_statement_actual_parameter_part(p[1],p[2])

def p_code_statement(p):
    '''code_statement : qualified_expression SEMICOLON
    '''
    p[0] = ga.c_code_statement(p[1])

def p_exit_statement(p):
    '''exit_statement : EXIT SEMICOLON
    | EXIT name SEMICOLON 
    '''
    if len(p[0]) == 3:
        p[0] = ga.c_exit_statement()
    else:
        p[0] = ga.c_exit_statement_name(p[1])

def p_null_statement(p):
    '''null_statement : NULL '''
    p[0] = ga.c_null_statement()

def p_assignment_statement(p):
    ''' assignment_statement : name ASSIGN expression SEMICOLON
    '''
    p[0] = ga.c_assignment_statement(p[1], p[3])

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