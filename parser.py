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
        [designator]
        ';'
    '''

def p_designator(p):
    ''' designator: [name "."] ( identifier|operator_symbol ) '''

def p_subprogram_specification(p):
    ''' subprogram_specification: 'procedure' defining_program_unit_name '''

def p_declarative_part(p):
    ''' declarative_part: { basic_declarative_item | subprogram_body } '''

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

#------------------------------------------------------------------------

#  PARTE DO MITO

#------------------------------------------------------------------------

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

#------------------------------------------------------------------------

#  PARTE DO MITO

#------------------------------------------------------------------------
