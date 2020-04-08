from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

'''
Exp e classes concretas
'''
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitMulExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitPotExp(self)


class CallExp(Exp):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        visitor.visitCallExp(self)

class AssignExp(Exp):
    def __init__(self, assign):
        self.assign = assign
    def accept(self, visitor):
        visitor.visitAssignExp(self)


class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitIdExp(self)


'''
Call e classes concretas
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        visitor.visitParamsCall(self)

class SimpleCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitSimpleCall(self)


'''
Params e classes concretas
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitSingleParam(self)


'''
Assign e classes concretas
'''

class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignAss(Assign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        visitor.visitAssignAss(self)

class identfier_list(Params):
    #''' identifier_list: {"," identifier }'''
    def __init__(self, identifier):
    def accept(self, visitor):

class loop_statement(Params):
   def __init__(self):
   def accept(self, visitor):

class if_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class sequence_of_statements(Params):
    def __init__(self):
    def accept(self, visitor):

class statement(Params):
    def __init__(self):
    def accept(self, visitor):

class compound(Params):
    def __init__(self):
    def accept(self, visitor):

class compound_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class discrete_subtype_definition(Params):
    def __init__(self):
    def accept(self, visitor):

class simple_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class entry_call_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class code_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class exit_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class null_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class assignment_statement(Params):
    def __init__(self):
    def accept(self, visitor):

class designator(Params):
    def __init__(self):
    def accept(self, visitor):

class subprogram_spaecification(Params):
    def __init__(self):
    def accept(self, visitor):

class declarative_part(Params):
    def __init__(self):
    def accept(self, visitor):

class basic_declarative_item(Params):
    def __init__(self):
    def accept(self, visitor):

class represation_clause(Params):
    def __init__(self):
    def accept(self, visitor):

class direct_name(Params):
    def __init__(self):
    def accept(self, visitor):

class attribute_definition_clause(Params):
    def __init__(self):
    def accept(self, visitor):

class element_name(Params):
    def __init__(self):
    def accept(self, visitor):

class indexed_component(Params):
    def __init__(self):
    def accept(self, visitor):

class type_conversion(Params):
    def __init__(self):
    def accept(self, visitor):

class selected_component(Params):
    def __init__(self):
    def accept(self, visitor):

class attribute_designator(Params):
    def __init__(self):
    def accept(self, visitor):

class expression(Params):
    def __init__(self):
    def accept(self, visitor):

class relation(Params):
    def __init__(self):
    def accept(self, visitor):

class simple_expression(Params):
    def __init__(self):
    def accept(self, visitor):

class term(Params):
    def __init__(self):
    def accept(self, visitor):

class factor(Params):
    def __init__(self):
    def accept(self, visitor):

class primary(Params):
    def __init__(self):
    def accept(self, visitor):

class qualified_expression(Params):
    def __init__(self):
    def accept(self, visitor):

class named_array_aggregate(Params):
    def __init__(self):
    def accept(self, visitor):

class array_component_association(Params):
    def __init__(self):
    def accept(self, visitor):

class discrete_choice_list(Params):
    def __init__(self):
    def accept(self, visitor):

class discrete_choice(Params):
    def __init__(self):
    def accept(self, visitor):

class subtype_identification(Params):
    def __init__(self):
    def accept(self, visitor):

class constraint(Params):
    def __init__(self):
    def accept(self, visitor):

class discriminant_constraint(Params):
    def __init__(self):
    def accept(self, visitor):

class discriminant_association(Params):
    def __init__(self):
    def accept(self, visitor):

class index_constraint(Params):
    def __init__(self):
    def accept(self, visitor):

class digits_constraint(Params):
    def __init__(self):
    def accept(self, visitor):

class range_constraint(Params):
    def __init__(self):
        def accept(self, visitor):

class range(Params):
    def __init__(self):
    def accept(self, visitor):

class range_attribute_reference(Params):
    def __init__(self):
    def accept(self, visitor):

class range_attribute_designator(Params):
    def __init__(self):
    def accept(self, visitor):

class name(Params):
    def __init__(self):
    def accept(self, visitor):

class slice(Params):
    def __init__(self):
    def accept(self, visitor):

class funcion_call(Params):
    def __init__(self):
    def accept(self, visitor):

class actual_parameter_part(Params):
    def __init__(self):
    def accept(self, visitor):

class parameter_association(Params):
    def __init__(self):
    def accept(self, visitor):

class selector_name(Params):
    def __init__(self):
    def accept(self, visitor):

class character_literal(Params):
    def __init__(self):
    def accept(self, visitor):

class enumeration_represation_clause(Params):
    def __init__(self):
    def accept(self, visitor):

class use_clause(Params):
    def __init__(self):
    def accept(self, visitor):

class basic_declaration(Params):
    def __init__(self):
    def accept(self, visitor):

class subprogram_declaration(Params):
    def __init__(self):
    def accept(self, visitor):

class subprogram_specification(Params):
    def __init__(self):
    def accept(self, visitor):

class defining_program_unit_name(Params):
    def __init__(self):
    def accept(self, visitor):
