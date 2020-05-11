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
class a_attribute_reference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_attribute_reference(a_attribute_reference):
    def __init__(self,name,attribute_designator):
        self.name = name
        self.attribute_designator = attribute_designator
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
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_minus_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_concat_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_plus_plus_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_plus_minus_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_plus_concat_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_minus_plus_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_minus_minus_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
    def accept(self, visitor):
        pass

class c_simple_expression_minus_concat_loop(a_simple_expression):
    def __init__(self,term1,term2,simple_expression):
        self.term1 = term1
        self.term2 = term2
        self.simple_expression = simple_expression
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

class a_discriminant_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_discriminant_constraint(a_discriminant_constraint):
    def __init__(self, discriminant_association):
        self.discriminant_association = discriminant_association
    def accept(self, visitor):
        pass

class c_discriminant_constraint_loop(a_discriminant_constraint): 
    def __init__(self, discriminant_association1, discriminant_association2, discriminant_constraint):
        self.discriminant_association1 = discriminant_association1
        self.discriminant_association2 = discriminant_association2
        self.discriminant_constraint = discriminant_constraint
    def accept(self, visitor):
        pass
#---------------------------------------------

class a_discriminant_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_discriminant_association(a_discriminant_association):
    def __init__(self, selector_name1, selector_name2, expression):
        self.selector_name1 = selector_name1
        self.selector_name2 = selector_name2
        self.expression = expression
    def accept(self, visitor):
        pass

class c_discriminant_association_loop(a_discriminant_association):
    def __init__(self, selector_name1, selector_name2, expression, discriminant_association):
        self.selector_name1 = selector_name1
        self.selector_name2 = selector_name2
        self.expression = expression
        self.discriminant_association = discriminant_association
    def accept(self, visitor):
        pass

class c_discriminant_association_pipe(a_discriminant_association):
    def __init__(self, selector_name):
        self.selector_name = selector_name
    def accept(self, visitor):
        pass

class c_discriminant_association_expression(a_discriminant_association):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass
#----------------------------------------------

class a_index_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_index_constraint(a_index_constraint):
    def __init__(self, discrete_range):
        self.discrete_range = discrete_range
    def accept(self, visitor):
        pass

class c_index_constraint_loop(a_index_constraint):
    def __init__(self, discrete_range1, discrete_range2, index_constraint):
        self.discrete_range1 = discrete_range1
        self.discrete_range2 = discrete_range2
        self.index_constraint = index_constraint
    def accept(self, visitor):
        pass

#----------------------------------------------

class a_digits_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_digits_constraint(a_digits_constraint):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass

class c_digits_constraint_range(a_digits_constraint):
    def __init__ (self, expression, range_constraint):
        self.expression = expression
        self.range_constraint = range_constraint
    def accept(self, visitor):
        pass

#----------------------------------------------    

class a_range_constraint(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_range_constraint(a_range_constraint):
    def __init__ (self, range):
        self.range = range
    def accept(self, visitor):
        pass

#----------------------------------------------

class a_range(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_range_attribute(a_range):
    def __init__(self, range_attribute_reference):
        self.range_attribute_reference = range_attribute_reference
    def accept(self, visitor):
        pass

class c_range_simple_expression(a_range):
    def __init__(self, simple_expression1,simple_expression2):
        self.simple_expression1 = simple_expression1
        self.simple_expression2 = simple_expression2
    def accept(self, visitor):
        pass

#---------------------------------------------    

class a_range_attribute_reference(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_range_attribute_reference(a_range_attribute_reference):
    def __init__(self, name, range_attribute_designator):
        self.name = name
        self.range_attribute_designator = range_attribute_designator
    def accept(self, visitor):
        pass

#------------------------------------------

class a_range_attribute_designator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_range_attribute_designator(a_range_attribute_designator):
    def __init__(self):
        pass
    def accept(self, visitor):
        pass

class c_range_attribute_designator_expression(a_range_attribute_designator):
    def __init__(self,expression):
        self.expression = expression
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

class a_slice(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_slice(a_slice):
    def __init__(self,name, discrete_range):
        self.name = name
        self.a_discrete_range = discrete_range
    def accept(self, visitor):
        pass

#------------------------------------------

class a_function_call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_function_call(a_function_call):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class c_function_call_actual_parameter_part(a_function_call):
    def __init__(self,name, actual_parameter_part):
        self.name = name
        self.actual_parameter_part = actual_parameter_part
    def accept(self, visitor):
        pass


#------------------------------------------

class a_actual_parameter_part(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_actual_parameter_part_loop(a_actual_parameter_part):
    def __init__(self,parameter_association,actual_parameter_part):
        self.parameter_association = parameter_association 
        self.actual_parameter_part = actual_parameter_part
    def accept(self, visitor):
        pass

class c_actual_parameter_part_paren(a_actual_parameter_part):
    def __init__(self,parameter_association):
        self.parameter_association = parameter_association
    def accept(self, visitor):
        pass

class c_actual_parameter_part_comma(a_actual_parameter_part):
    def __init__(self,parameter_association):
        self.parameter_association = parameter_association
    def accept(self, visitor):
        pass

#------------------------------------------

class a_parameter_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_parameter_association_expression(a_parameter_association):
    def __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

class c_parameter_association_name(a_parameter_association):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class c_parameter_association_selector_name_expression(a_parameter_association):
    def __init__(self,selector_name,expression):
        self.selector_name = selector_name
        self.expression = expression
    def accept(self, visitor):
        pass

class c_parameter_association_selector_name_name(a_parameter_association):
    def __init__(self,selector_name,name):
        self.selector_name = selector_name
        self.name = name
    def accept(self, visitor):
        pass

#------------------------------------------

class a_selector_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_selector_name_identifier(a_selector_name):
    def __init__(self,identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_selector_name_character_literal(a_selector_name):
    def __init__(self,character_literal):
        self.character_literal = character_literal
    def accept(self, visitor):
        pass

class c_selector_name_operator_symbol(a_selector_name):
    def __init__(self,operator_symbol):
        self.operator_symbol = operator_symbol
    def accept(self, visitor):
        pass

#------------------------------------------

class a_character_literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_character_literal(metaclass=ABCMeta):
    def __init__(self,graphic_character):
        self.graphic_character = graphic_character
    def accept(self, visitor):
        pass

#------------------------------------------

class a_enumeration_representation_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_enumeration_representation_clause(a_enumeration_representation_clause):
    def __init__(self,direct_name,named_array_aggregate):
        self.direct_name = direct_name
        self.named_array_aggregate = named_array_aggregate
    def accept(self, visitor):
        pass

#------------------------------------------
class a_incomplete_type_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_incomplete_type_declaration(a_incomplete_type_declaration):
    def __init__(self,identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_incomplete_type_declaration_discriminant_part(a_incomplete_type_declaration):
    def __init__(self,identifier,discriminant_part):
        self.identifier = identifier
        self.discriminant_part = discriminant_part
    def accept(self, visitor):
        pass
#------------------------------------------

class a_basic_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_basic_declaration_incomplete_type_declaration(a_basic_declaration):
    def __init__(self,incomplete_type_declaration):
        self.incomplete_type_declaration = incomplete_type_declaration
    def accept(self, visitor):
        pass

class c_basic_declaration_number_declaration(a_basic_declaration):
    def __init__(self,number_declaration):
        self.number_declaration = number_declaration
    def accept(self, visitor):
        pass

class c_basic_declaration_subprogram_declaration(a_basic_declaration):
    def __init__(self,subprogram_declaration):
        self.subprogram_declaration = subprogram_declaration
    def accept(self, visitor):
        pass

#------------------------------------------

class a_use_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class a_use_clause_use(a_use_clause):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class a_use_clause_use_loop(a_use_clause):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def accept(self, visitor):
        pass

class a_use_clause_type(a_use_clause):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class a_use_clause_type_loop(a_use_clause):
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def accept(self, visitor):
        pass


#------------------------------------------

class a_subprogram_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_subprogram_declaration(a_subprogram_declaration):
    def __init__(self,subprogram_specification):
       self.subprogram_specification = subprogram_specification
    def accept(self, visitor):
        pass


#-----------------------------------------------------------#
class a_subprogram_specification(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_subprogram_specification(a_subprogram_specification):
    def __init__(self,subprogram_specification):
        self.subprogram_specification = subprogram_specification
    def accept(self, visitor):
        pass

#----------------------------------------------------------#
class a_defining_program_unit_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_defining_program_unit_name_identifier(a_defining_program_unit_name):
    def __init__(self,identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_defining_program_unit_name_name_identifier(a_defining_program_unit_name):
    def __init__(self,name,identifier):
        self.name = name
        self.identifier = identifier
    def accept(self, visitor):
        pass

#---------------------------------------------------------#

class a_number_declaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_number_declaration(a_number_declaration):
    def __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

#---------------------------------------------------------#
##################################################################################################################
class a_identifier_list(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
       pass

class c_idetifier_list(a_identifier_list):
    def __init__(self, identifier_list):
       self.identifier_list = identifier_list
    def accept(self, visitor):
        pass
##################################################################################################################
#---------------------------------------------------------#

class a_loop_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_loop_statement(a_loop_statement):
    def __init__(self,sequence_of_statements):
      self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
       pass

class c_loop_statement_name(a_loop_statement):
    def __init__(self,sequence_of_statements,name):
      self.sequence_of_statements = sequence_of_statements
      self.name = name
    def accept(self, visitor):
       pass

class c_loop_statement_while(a_loop_statement):
    def __init__(self,expression, sequence_of_statements):
      self.expression = expression
      self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
       pass

class c_loop_statement_while_name(a_loop_statement):
    def __init__(self,expression, sequence_of_statements,name):
      self.expression = expression
      self.sequence_of_statements = sequence_of_statements
      self.name = name
    def accept(self, visitor):
       pass

class c_loop_statement_for(a_loop_statement):
    def __init__(self,identifier,discrete_subtype_definition, sequence_of_statements):
      self.discrete_subtype_definition = discrete_subtype_definition
      self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
       pass  

class c_loop_statement_for_name(a_loop_statement):
    def __init__(self,identifier,discrete_subtype_definition, sequence_of_statements,name):
      self.discrete_subtype_definition = discrete_subtype_definition
      self.sequence_of_statements = sequence_of_statements
      self.name = name
    def accept(self, visitor):
       pass   

class c_loop_statement_for_reverse(a_loop_statement):
    def __init__(self,identifier,discrete_subtype_definition, sequence_of_statements):
      self.discrete_subtype_definition = discrete_subtype_definition
      self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
       pass  

class c_loop_statement_for_reverse_name(a_loop_statement):
    def __init__(self,identifier,discrete_subtype_definition, sequence_of_statements,name):
      self.discrete_subtype_definition = discrete_subtype_definition
      self.sequence_of_statements = sequence_of_statements
      self.name = name
    def accept(self, visitor):
       pass   

#----------------------------------------------------------#

class a_if_statement(metaclass=ABCMeta):
   @abstractmethod
   def accept(self, visitor):
       pass

class c_if_statement(a_if_statement):
    def __init__(self, expression,sequence_of_statements):
        self.expression = expression
        self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
        pass

class c_if_statement_elsif(a_if_statement):
    def __init__(self,expression1,sequence_of_statements1,expression2,sequence_of_statements2):
        self.expression1 = expression1
        self.sequence_of_statements1 = sequence_of_statements1
        self.expression2 = expression2
        self.sequence_of_statements2 = sequence_of_statements2
    def accept(self, visitor):
        pass

class c_if_statement_elsif_loop(a_if_statement):
    def __init__(self,expression1,sequence_of_statements1,expression2,sequence_of_statements2,if_statement):
        self.expression1 = expression1
        self.sequence_of_statements1 = sequence_of_statements1
        self.expression2 = expression2
        self.sequence_of_statements2 = sequence_of_statements2
        self.if_statement = if_statement
    def accept(self, visitor):
        pass

class c_if_statement_else(a_if_statement):
    def __init__(self, expression,sequence_of_statements1,sequence_of_statements2):
        self.expression = expression
        self.sequence_of_statements1 = sequence_of_statements1
        self.sequence_of_statements2 = sequence_of_statements2
    def accept(self, visitor):
        pass

#---------------------------------------------------------#


class a_sequence_of_statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_sequence_of_statements(a_sequence_of_statements):
    def __init__(self,statement):
        self.statement = statement
    def accept(self, visitor):
        pass

class c_sequence_of_statements_loop(a_sequence_of_statements):
    def __init__(self,statement,sequence_of_statements):
        self.statement = statement
        self.sequence_of_statements = sequence_of_statements
    def accept(self, visitor):
        pass


#------------------------------------------

class a_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_statement_simple_statement(a_statement):
    def __init__(self,simple_statement):
        self.simple_statement = simple_statement
    def accept(self, visitor):
        pass

class c_statement_compound_statement(a_statement):
    def __init__(self,compound_statement):
        self.compound_statement = compound_statement
    def accept(self, visitor):
        pass

#------------------------------------------

class a_compound_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_compound_statement_if_statement(a_compound_statement):
    def __init__(self,if_statement):
        self.if_statement = if_statement
    def accept(self, visitor):
        pass

class c_compound_statement_loop_statement(a_compound_statement):
    def __init__(self,loop_statement):
        self.loop_statement = loop_statement
    def accept(self, visitor):
        pass

#------------------------------------------

class a_discrete_subtype_definition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_discrete_subtype_definition_subtype_indication(a_discrete_subtype_definition):
    def __init__(self,subtype_indication):
        self.subtype_indication = subtype_indication
    def accept(self, visitor):
        pass

class c_discrete_subtype_definition_range(a_discrete_subtype_definition):
    def __init__(self,range):
        self.range = range
    def accept(self, visitor):
        pass

#------------------------------------------

class a_simple_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_simple_statement_null_statement(a_simple_statement):
    def __init__(self,null_statement):
        self.null_statement = null_statement
    def accept(self, visitor):
        pass

class c_simple_statement_assignment_statement(a_simple_statement):
    def __init__(self,assignment_statement):
        self.assignment_statement = assignment_statement
    def accept(self, visitor):
        pass

class c_simple_statement_exit_statement(a_simple_statement):
    def __init__(self,exit_statement):
        self.exit_statement = exit_statement
    def accept(self, visitor):
        pass

class c_simple_statement_procedure_call_statement(a_simple_statement):
    def __init__(self,procedure_call_statement):
        self.procedure_call_statement = procedure_call_statement
    def accept(self, visitor):
        pass

class c_simple_statement_return_statement(a_simple_statement):
    def __init__(self,return_statement):
        self.return_statement = return_statement
    def accept(self, visitor):
        pass

class c_simple_statement_entry_call_statement(a_simple_statement):
    def __init__(self,entry_call_statement):
        self.entry_call_statement = entry_call_statement
    def accept(self, visitor):
        pass

class c_simple_statement_code_statement(a_simple_statement):
    def __init__(self,code_statement):
        self.code_statement = code_statement
    def accept(self, visitor):
        pass

#------------------------------------------

class a_entry_call_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_entry_call_statement(a_entry_call_statement):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

class c_entry_call_statement_actual_parameter_part(a_entry_call_statement):
    def __init__(self,name,actual_parameter_part):
        self.name = name
        self.actual_parameter_part = actual_parameter_part
    def accept(self, visitor):
        pass

#------------------------------------------

class a_code_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_code_statement(a_code_statement):
    def __init__(self,qualified_expression):
        self.qualified_expression = qualified_expression
    def accept(self, visitor):
        pass

#------------------------------------------

class a_exit_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_exit_statement(a_exit_statement):
    def __init__(self):
        pass
    def accept(self, visitor):
        pass

class c_exit_statement_name(a_exit_statement):
    def __init__(self,name):
        self.name = name
    def accept(self, visitor):
        pass

#------------------------------------------

class a_null_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_null_statement(a_null_statement):
    def __init__(self):
        pass
    def accept(self, visitor):
        pass
    
#------------------------------------------

class a_assignment_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_assignment_statement(a_assignment_statement):
    def __init__(self,name,expression):
        self.name = name
        self.expression = expression
    def accept(self, visitor):
        pass
