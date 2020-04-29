from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor


class a_subprogram_body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class c_subprogram_body(a_subprogram_body): #indica que a classe implementa a classe abstrata  
    def __init__(self,subprogram_specification,declarative_part,sequence_of_statements,designator):
        self.subprogram_specification = subprogram_specification
        self.declarative_part = declarative_part
        self.sequence_of_statements = sequence_of_statements
        self.designator = designator
    def accept(self,visitor):
        pass

#------------------------------------------

class a_designator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_designator_name_identfier(a_designator):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_designator_name_operator_symbol(a_designator):
    def __init__(self, name, operator_symbol):
        self.name = name
        self.operator_symbol = operator_symbol
    def accept(self, visitor):
        pass

class c_designator_identfier(a_designator):
    def __init__(self, identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_designator_operator_symbol(a_designator):
    def __init__(self, operator_symbol):
        self.operator_symbol = operator_symbol
    def accept(self, visitor):
        pass

#------------------------------------------

class a_subprogram_specification(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_subprogram_specification(a_subprogram_specification):
    def __init__(self,defining_program_unit_name):
        self.defining_program_unit_name = defining_program_unit_name
    def accept(self, visitor):
        pass

#------------------------------------------

class a_declarative_part(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_declarative_part_basic_declarative_item(a_declarative_part):
    def __init__(self,basic_declarative_item): 
        self.basic_declarative_item = basic_declarative_item
    def accept(self, visitor):
        pass

class c_declarative_part_subprogram_body(a_declarative_part):
    def __init__(self,subprogram_body): 
        self.subprogram_body = subprogram_body
    def accept(self, visitor):
        pass

class c_declarative_part_basic_declarative_item_loop(a_declarative_part):
    def __init__(self,basic_declarative_item,declarative_part): 
        self.basic_declarative_item = basic_declarative_item
        self.declarative_part = declarative_part
    def accept(self, visitor):
        pass

class c_declarative_part_subprogram_body_loop(a_declarative_part):
    def __init__(self,subprogram_body,declarative_part): 
        self.subprogram_body = subprogram_body
        self.declarative_part = declarative_part
    def accept(self, visitor):
        pass

#------------------------------------------

class a_basic_declarative_item(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_basic_declarative_item_basic_declaration(a_basic_declarative_item):
    def __init__(self,basic_declaration):
        self.basic_declaration = basic_declaration
    def accept(self, visitor):
        pass

class c_basic_declarative_item_representation_clause(a_basic_declarative_item):
    def __init__(self,representation_clause):
        self.representation_clause = representation_clause
    def accept(self, visitor):
        pass

class c_basic_declarative_item_use_clause(a_basic_declarative_item):
    def __init__(self,use_clause):
        self.use_clause = use_clause
    def accept(self, visitor):
        pass

#------------------------------------------

class a_representation_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass        

class c_representation_clause_attribute_definition_clause(a_representation_clause):
    def __init__(self,attribute_definition_clause):
        self.attribute_definition_clause = attribute_definition_clause
    def accept(self, visitor):
        pass

class c_representation_clause_enumeration_representation_clause(a_representation_clause):
    def __init__(self,enumeration_representation_clause):
        self.enumeration_representation_clause = enumeration_representation_clause
    def accept(self, visitor):
        pass

#------------------------------------------

class a_direct_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_direct_name_identifier(a_direct_name):
    def __init__(self,identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_direct_name_operator_symbol(a_direct_name):
    def __init__(self,operator_symbol):
        self.operator_symbol = operator_symbol
    def accept(self, visitor):
        pass

#------------------------------------------

class a_attribute_definition_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_attribute_definition_clause_expression(a_attribute_definition_clause):
    def  __init__(self,name,attribute_designator,expression):
        self.name = name
        self.a_attribute_designator = attribute_designator
        self.expression = expression
    def accept(self, visitor):
        pass

class c_attribute_definition_clause_name(a_attribute_definition_clause):
    def  __init__(self,name1,attribute_designator,name2):
        self.name1 = name1
        self.attribute_designator = attribute_designator
        self.name2 = name2
    def accept(self, visitor):
        pass

#------------------------------------------

class a_indexed_component(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_indexed_component(a_indexed_component):
    def __init__(self,name,expression):
        self.name = name
        self.expression = expression
    def accept(self, visitor):
        pass

class c_indexed_component_loop(a_indexed_component):
    def __init__(self,name, expression,indexed_component):
        self.name = name
        self.expression = expression
        self.indexed_component = indexed_component
    def accept(self, visitor):
        pass

#------------------------------------------

class a_type_conversion(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
class c_type_conversion_name(a_type_conversion):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def accept(self, visitor):
        pass
class c_type_conversion_expression(a_type_conversion):
    def __init__(self,name,expression):
        self.name = name
        self.expression = expression
    def accept(self, visitor):
        pass

#------------------------------------------
#####################################
class a_selected_component(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_selected_component(a_selected_component):
    def __init__(self,name,selector_name):
        self.name = name
        self.selector_name = selector_name
    def accept(self, visitor):
        pass

#------------------------------------------
class a_attribute_designator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_attribute_designator_identifier(a_attribute_designator):
    def __init__(self,identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_attribute_designator_identifier_expression(a_attribute_designator):
    def __init__(self,identifier,expression):
        self.identifier = identifier
        self.expression = expression
    def accept(self, visitor):
        pass
#------------------------------------------
class a_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_expression_and(a_expression):
    def __init__(self,relation1,relation2):
        self.relation1 = relation1
        self.relation2 = relation2
    def accept(self, visitor):
        pass

class c_expression_and_loop(a_expression):
    def __init__(self,relation1,relation2,expression):
        self.relation1 = relation1
        self.relation2 = relation2
        self.expression = expression
    def accept(self, visitor):
        pass

class c_expression_and_then(a_expression):
    def __init__(self,relation1,relation2):
        self.relation1 = relation1
        self.relation2 = relation2
    def accept(self, visitor):
        pass

class c_expression_and_then_loop(a_expression):
    def __init__(self,relation1,relation2,expression):
        self.relation1 = relation1
        self.relation2 = relation2
        self.expression = expression
    def accept(self, visitor):
        pass

class c_expression_or(a_expression):
    def __init__(self,relation1,relation2):
        self.relation1 = relation1
        self.relation2 = relation2
    def accept(self, visitor):
        pass

class c_expression_or_loop(a_expression):
    def __init__(self,relation1,relation2,expression):
        self.relation1 = relation1
        self.relation2 = relation2
        self.expression = expression
    def accept(self, visitor):
        pass

class c_expression_or_else(a_expression):
    def __init__(self,relation1,relation2):
        self.relation1 = relation1
        self.relation2 = relation2
    def accept(self, visitor):
        pass

class c_expression_or_else_loop(a_expression):
    def __init__(self,relation1,relation2,expression):
        self.relation1 = relation1
        self.relation2 = relation2
        self.expression = expression
    def accept(self, visitor):
        pass

class c_expression_xor(a_expression):
    def __init__(self,relation1,relation2):
        self.relation1 = relation1
        self.relation2 = relation2
    def accept(self, visitor):
        pass

class c_expression_xor_loop(a_expression):
    def __init__(self,relation1,relation2,expression):
        self.relation1 = relation1
        self.relation2 = relation2
        self.expression = expression
    def accept(self, visitor):
        pass
#------------------------------------------
class a_relation(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_relation(a_relation):
    def __init__(self,simpĺe_expression):
        self.simpĺe_expression = simpĺe_expression
    def accept(self, visitor):
        pass

class c_relation_equal(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_not_equal(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_less_than(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_less_than_equal(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_greater_than(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_greater_than_equal(a_relation):
    def __init__(self,simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

class c_relation_in_range(a_relation):
    def __init__(self,simple_expression,range):
        self.simple_expression = simple_expression
        self.range = range
    def accept(self, visitor):
        pass

class c_relation_in_name(a_relation):
    def __init__(self,simple_expression,name):
        self.simple_expression = simple_expression
        self.name = name
    def accept(self, visitor):
        pass

class c_relation_not_in_range(a_relation):
    def __init__(self,simple_expression,range):
        self.simple_expression = simple_expression
        self.range = range
    def accept(self, visitor):
        pass

class c_relation_not_in_name(a_relation):
    def __init__(self,simple_expression,name):
        self.simple_expression = simple_expression
        self.name = name
    def accept(self, visitor):
        pass

#------------------------------------------
class a_simple_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_simple_expression_plus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_concat(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_plus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_minus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_concat(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_plus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_minus(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_concat(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_concat_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_plus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_minus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_plus_concat_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_plus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_minus_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

class c_simple_expression_minus_concat_loop(a_simple_expression):
    def __init__(self,term1,term2):
        self.term1 = term1
        self.term2 = term2
    def accept(self, visitor):
        pass

#------------------------------------------

class a_term(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class c_term(a_term):
    def __init__(self,factor):
        self.factor = factor
    def accept(self, visitor):
        pass

class c_term_times(a_term):
    def __init__(self,factor1,factor2,term):
        self.factor1 = factor1
        self.factor2 = factor2
        self.term = term
    def accept(self, visitor):
        pass

class c_term_divide(a_term):
    def __init__(self,factor1,factor2,term):
        self.factor1 = factor1
        self.factor2 = factor2
        self.term = term
    def accept(self, visitor):
        pass

class c_term_mod(a_term):
    def __init__(self,factor1,factor2,term):
        self.factor1 = factor1
        self.factor2 = factor2
        self.term = term
    def accept(self, visitor):
        pass

class c_term_rem(a_term):
    def __init__(self,factor1,factor2,term):
        self.factor1 = factor1
        self.factor2 = factor2
        self.term = term
    def accept(self, visitor):
        pass

#------------------------------------------

class a_factor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_factor(a_factor):
    def __init__(self,primary):
        self.primary = primary
    def accept(self, visitor):
        pass

class c_factor_power(a_factor):
    def __init__(self,primary1,primary2):
        self.primary1 = primary1
        self.primary2 = primary2
    def accept(self, visitor):
        pass

#------------------------------------------

class a_primary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_primary_numeric_literal(a_primary):
    def __init__(self,numeric_literal):
        self.numeric_literal = numeric_literal
    def accept(self, visitor):
        pass

class c_primary_null(a_primary):
    def __init__(self):
        pass
    def accept(self, visitor):
        pass

class c_primary_string_literal(a_primary):
    def __init__(self,string_literal):
        self.string_literal = string_literal
    def accept(self, visitor):
        pass

class c_primary_named_array_aggregate(a_primary):
    def __init__(self,named_array_aggregate):
        self.named_array_aggregate = named_array_aggregate
    def accept(self, visitor):
        pass

class c_primary_name(a_primary):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class c_primary_qualified_expression(a_primary):
    def __init__(self,qualified_expression):
        self.qualified_expression = qualified_expression
    def accept(self, visitor):
        pass

class c_primary_expression(a_primary):
    def __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

#------------------------------------------

class a_qualified_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_qualified_expression_expression(a_qualified_expression):
    def __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

class c_qualified_expression_named_array_aggregate(a_qualified_expression):
    def __init__(self,named_array_aggregate):
        self.named_array_aggregate = named_array_aggregate
    def accept(self, visitor):
        pass

#------------------------------------------

class a_named_array_aggregate(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_named_array_aggregate(a_named_array_aggregate):
    def __init__(self,array_component_association):
        self.array_component_association = array_component_association
    def accept(self, visitor):
        pass

class c_named_array_aggregate_loop(a_named_array_aggregate):
    def __init__(self,array_component_association1,array_component_association2,named_array_aggregate):
        self.array_component_association1 = array_component_association1
        self.array_component_association2 = array_component_association2
        self.named_array_aggregate = named_array_aggregate
    def accept(self, visitor):
        pass

#------------------------------------------

class a_array_component_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_array_component_association(a_array_component_association):
    def __init__(self,discrete_choice,expression):
        self.discrete_choice = discrete_choice
        self.expression = expression
    def accept(self, visitor):
        pass

#------------------------------------------

class a_discrete_choice_list(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_discrete_choice_list(a_discrete_choice_list):
    def __init__(self,discrete_choice):
        self.discrete_choice = discrete_choice
    def accept(self, visitor):
        pass

class c_discrete_choice_list_loop(a_discrete_choice_list):
    def __init__(self,discrete_choice1,discrete_choice2,discrete_choice_list):
        self.discrete_choice1 = discrete_choice1
        self.discrete_choice2 = discrete_choice2
        self.discrete_choice_list = discrete_choice_list
    def accept(self, visitor):
        pass

#------------------------------------------

class a_discrete_choice(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_discrete_choice_expression(a_discrete_choice):
    def __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

class c_discrete_choice_discrete_range(a_discrete_choice):
    def __init__(self,discrete_range):
        self.discrete_range = discrete_range
    def accept(self, visitor):
        pass

#------------------------------------------

class a_discrete_range(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class c_discrete_range_range(a_discrete_range):
    def __init__(self,range):
        self.range = range
    def accept(self,visitor):
        pass

class c_discrete_range_subtype_indicator(a_discrete_range):
    def __init__(self,subtype_indicator):
        self.subtype_indicator = subtype_indicator
    def accept(self,visitor):
        pass

#------------------------------------------

class a_subtype_indicator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_subtype_indicator_name(a_subtype_indicator):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class c_subtype_indicator_name_constraint(a_subtype_indicator):
    def __init__(self,name,constraint):
        self.name = name
        self.constraint = constraint
    def accept(self, visitor):
        pass

#------------------------------------------

class a_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_constraint_range_constraint(a_constraint):
    def __init__(self,range_constraint):
        self.range_constraint = range_constraint
    def accept(self, visitor):
        pass

class c_constraint_digits_constraint(a_constraint):
    def __init__(self,digits_constraint):
        self.digits_constraint = digits_constraint
    def accept(self, visitor):
        pass

class c_constraint_index_constraint(a_constraint):
    def __init__(self,index_constraint):
        self.index_constraint = index_constraint
    def accept(self, visitor):
        pass

class c_constraint_discriminant_constraint(a_constraint):
    def __init__(self,discriminant_constraint):
        self.discriminant_constraint = discriminant_constraint
    def accept(self, visitor):
        pass

#------------------------------------------
##############
class sequence_of_statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class identfier_list(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class loop_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class if_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class compound(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class compound_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class discrete_subtype_definition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class simple_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class entry_call_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class code_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class exit_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class null_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class assignment_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class selected_component(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class discriminant_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class discriminant_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class index_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class digits_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class range_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class range(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class range_attribute_reference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class range_attribute_designator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

#------------------------------------------

class a_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_name_direct_name(a_name):
    def __init__(self,direct_name):
        self.a_direct_name = direct_name
    def accept(self, visitor):
        pass

class c_name_slice(a_name):
    def __init__(self,slice):
        self.slice = slice
    def accept(self, visitor):
        pass

class c_name_selected_component(a_name):
    def __init__(self,selected_component):
        self.selected_component = selected_component
    def accept(self, visitor):
        pass

class c_name_attribute_reference(a_name):
    def __init__(self,attribute_reference):
        self.attribute_reference = attribute_reference
    def accept(self, visitor):
        pass

class c_name_type_conversion(a_name):
    def __init__(self,type_conversion):
        self.type_conversion = type_conversion
    def accept(self, visitor):
        pass

class c_name_function_call(a_name):
    def __init__(self,function_call):
        self.function_call = function_call
    def accept(self, visitor):
        pass

class c_name_character_literal(a_name):
    def __init__(self,character_literal):
        self.character_literal = character_literal
    def accept(self, visitor):
        pass

class c_name_indexed_component(a_name):
    def __init__(self,indexed_component):
        self.indexed_component = indexed_component
    def accept(self, visitor):
        pass

#------------------------------------------

class slice(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class funcion_call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class actual_parameter_part(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class parameter_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class selector_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class character_literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class enumeration_representation_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class use_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class basic_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class subprogram_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class defining_program_unit_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
