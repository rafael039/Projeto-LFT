from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

class subprogram_body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class subprogram_specification(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class declarative_part(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class sequence_of_statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class designator(metaclass=ABCMeta):
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

class basic_declarative_item(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class represation_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class direct_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class attribute_definition_clause(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class element_name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class indexed_component(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class type_conversion(metaclass=ABCMeta):
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

class name(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

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

class enumeration_represation_clause(metaclass=ABCMeta):
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
