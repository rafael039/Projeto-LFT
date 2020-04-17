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

class c_designator_name_operation_symbol(a_designator):
    def __init__(self, name, operation_symbol):
        self.name = name
        self.operation_symbol = operation_symbol
    def accept(self, visitor):
        pass

class c_designator_identfier(a_designator):
    def __init__(self, identifier):
        self.identifier = identifier
    def accept(self, visitor):
        pass

class c_designator_operation_symbol(a_designator):
    def __init__(self, operation_symbol):
        self.operation_symbol = operation_symbol
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
    def __init__(self,basic_declarative_item,subprogram_body): 
        self.basic_declarative_item = basic_declarative_item
        self.subprogram_body = subprogram_body
    def accept(self, visitor):
        pass

class c_declarative_part_subprogram_body(a_declarative_part):
    def __init__(self,basic_declarative_item,subprogram_body): 
        self.basic_declarative_item = basic_declarative_item
        self.subprogram_body = subprogram_body
    def accept(self, visitor):
        pass

class c_declarative_part_basic_declarative_item_loop(a_declarative_part):
    def __init__(self,basic_declarative_item,subprogram_body,declarative_part): 
        self.basic_declarative_item = basic_declarative_item
        self.subprogram_body = subprogram_body
        self.declarative_part = declarative_part
    def accept(self, visitor):
        pass

class c_declarative_part_subprogram_body_loop(a_declarative_part):
    def __init__(self,basic_declarative_item,subprogram_body,declarative_part): 
        self.basic_declarative_item = basic_declarative_item
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

class c_representation_clause_enumeration_represation_clause(a_representation_clause):
    def __init__(self,enumeration_represation_clause):
        self.enumeration_represation_clause = enumeration_represation_clause
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

class c_direct_name_operation_symbol(a_direct_name):
    def __init__(self,operation_symbol):
        self.operation_symbol = operation_symbol
    def accept(self, visitor):
        pass

#------------------------------------------

class a_attribute_definition_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_attribute_definition_clause_expression(a_attribute_definition_clause):
    def  __init__(self,expression):
        self.expression = expression
    def accept(self, visitor):
        pass

class c_attribute_definition_clause_name(a_attribute_definition_clause):
    def  __init__(self,name):
        self.name = name
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

class attribute_designator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class relation(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class simple_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class term(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class factor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class primary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class qualified_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class named_array_aggregate(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class array_component_association(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class discrete_choice_list(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class discrete_choice(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class subtype_identification(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class constraint(metaclass=ABCMeta):
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
