from abc import abstractmethod
from abc import ABCMeta
#from visitor import visitor

class a_program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class c_program(a_program):
    def __init__(self,decl,body): 
        self.decl = decl
        self.body = body
    def accept(self,visitor):
    pass

class c_program_decl(a_program):
    def __init__(self,body): 
        self.body = body
    def accept(self,visitor):
    pass

class a_subprogram(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass

class c_subprogram(a_subprogram):
    def __init__(self,decl_param,body):
        self.decl_param = decl_param
        self.body = body
    def accept(self,visitor):
        pass

class c_subprogram_decl(a_subprogram):
    def __init__(self,decl_param,decl,body):
        self.decl_param = decl_param
        self.body = body
    def accept(self,visitor):
        pass

class a_body(metaclass=ABCMeta):
    