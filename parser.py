import ply.yacc as yacc
from calclex import *
import gramAbstrata as ga
import visitor as vis

def p_subprogram_body(p):
    ''' subprogram_body: subprogram_specification
        'is'
        declarative_part
        'begin'
        sequence_of_statements
        'end'
        designator
        ';'
        | subprogram_specification
        'is'
        declarative_part
        'begin'
        sequence_of_statements
        'end'
        ';'
    '''

    if len(p) == 9:
        p[0] = c_subprogram_body(p[1],p[3],p[5],p[7])
    else:
        p[0] = c_subprogram_body(p[1],p[3],p[5],None)

def p_designator(p):
    ''' designator: [name "."] ( identifier | operator_symbol ) '''

def p_subprogram_specification(p):
    ''' subprogram_specification: 'procedure' defining_program_unit_name '''
    p[0] = c_subprogram_specification(p[2])

def p_declarative_part(p):
    # ocorrência de chaves = recursão
    ''' declarative_part: basic_declarative_item | subprogram_body 
        | basic_declarative_item declarative_part | subprogram_body declarative part
    '''

def p_basic_declarative_item(p):
    ''' basic_declarative_item: basic_declaration | representation_clause | use_clause '''

def p_representation_clause(p):
    ''' representation_clause: attribute_definition_clause | enumeration_represation_clause '''

def p_direct_name(p):
    ''' direct_name: identifier | operator_symbol '''

def p_attribute_definition_clause(p):
    ''' attribute_definition_name: 'for' name 'single_quote' attribute_designator 'use' expression ';' 
    'for' name  'single_quote' attribute designator 'use' element_name ';' '''

def p_element_name(p):
    ''' element_name: direct_name | slice | selected_component | attribute_reference | type_conversion
    | function_call | 'character_literal' | indexed_component'''

def p_indexed_component(p):
    ''' indexed_component: name"(" expression {"," expression } ")" '''

def p_type_conversion(p):
    ''' type_conversion: name"(" ( expression | name ) ")" ''' 

def p_selected_component(p):
    ''' select_component: name "." selector_name '''

def p_attribute_designator(p):
    ''' attribute_designator: ( identifier [" (" expression ")" ]) | "Digits" '''

def p_expression(p):
    ''' expression: relation { "and" relation} | relation { "and" "then" relation }
    | relation { "or" relation } | relation { "or" "else" relation } | relation { "xor" relation } '''

def p_relation(p):
    ''' relation: ( simple_expression [ ("=" | "/=" | "<" | "<=" | ">" | ">=" ) simple_expression ] )
    | (simple_exoression [ "not" ] "in" (range | name) ) '''

def p_simple_expression(p):
    ''' simple_epxression: [ ( "+" | "-") ] term { ( "+" | "-" | "&") term } '''

def p_term(p): 
    ''' term: factor { ( "*" | "/" | "mod"  | "rem" ) factor } '''

def p_factor(p):
    ''' factor: ( primary [ "**" primary ] ) '''

def p_primary(p):
    ''' primary: numeric_literal | "null" | string_literal | named_array_aggregate
    | name | qualified_expression | ("(" expression ")") ''' 

def p_qualified_expression(p):
    ''' qualified_expression: name"" ("("expression")")'''

def p_named_array_aggregate(p):
    ''' named_array_aggregate: "(" array_component_association {"," array_component_association } ")"'''

def p_array_component_association(p):
    ''' array_component_association: { "|" discrete_choice "=>" expression '''

def p_discrete_choice_list(p):
    ''' discrete_choice_list: expression | '''

def p_discrete_choice(p):
    ''' discrete_choice: expression | discrete_range'''

def p_subtype_indication(p):
    ''' subtype_indication: name[contraint]'''

def p_contraint(p):
    ''' constraint: range_constraint | digits_constraint | index_constraint | discriminant_constraint '''

def p_discriminant_contraint(p):
    ''' discrimination_constraint:  "(" discriminant_association { "," discriminant_association } ")" '''

def p_discriminant_association(p):
    ''' discriminant_association: [selector_name { "|" selector_name } "=>" ] expression '''

def p_index_constraint(p):
    ''' "(" discrete_range: { "," discrete_range } ")" '''

def p_digits_constraint(p):
    ''' digits_constraint: "digits  expression [range_constraint] "'''

def p_range_constraint(p):
    '''"range: range"'''

def p_range(p):
    '''range: (simple_expression ".." simple_expression )'''

def p_range_attribute_reference(p):
    ''' range_attribute_reference: name "" range_attribute_designator '''

def p_range_attribute_designator(p):
    ''' range_attribute_designator: "Range" ["(" expression ")"] '''

def p_name(p):
    ''' name: direct_name | indexed_component | slice | selected_component | attribute_reference 
    | type_conversion | function_call | character_literal '''

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
    '''if_statement: if expression 'then' sequence_of_statements { 'elsif' | expression 'then' sequence_of_statements }
    ['else'|| sequence_of_statements] 'end' 'if' ';' '''
    
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