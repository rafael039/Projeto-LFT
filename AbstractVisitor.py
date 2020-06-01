from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgram(self,program):
         pass

    @abstractmethod
    def visitSubprogram(self,subprogram):
        pass

    @abstractmethod
    def visitBody(self,body):
        pass

    @abstractmethod
    def visitDecl(self,decl):
        pass

    @abstractmethod
    def visitVar(self,var):
        pass

    @abstractmethod
    def visitVarLoop(self,var_loop):
        pass

    @abstractmethod
    def visitDeclParam(self,decl_param):
        pass

    @abstractmethod
    def visitParam(self,param):
        pass

    @abstractmethod
    def visitFunctionCall(self,function_call):
        pass

    @abstractmethod
    def visitFunctionCallExp(self,function_call_exp):
        pass
    
    @abstractmethod
    def visitParamPass(self,param_pass):
        pass
    
    @abstractmethod
    def visitValue(self,value):
        pass
    
    @abstractmethod
    def visitCmd(self,cmd):
        pass
    
    @abstractmethod
    def visitCmdLoop(self,cmd_loop):
        pass
    
    @abstractmethod
    def visitPuts(self,puts):
        pass
    
    @abstractmethod
    def visitIfStatement(self,if_statement):
        pass
    
    @abstractmethod
    def visitIfStatementLoop(self,if_statement_loop):
        pass
    
    @abstractmethod
    def visitRepeatStatement(self,repeat_statement):
        pass
    
    @abstractmethod
    def visitLoopStatement(self,loop_statement):
        pass
    
    @abstractmethod
    def visitWhileStatement(self,while_statement):
        pass
    
    @abstractmethod
    def visitForStatement(self,for_statement):
        pass
    
    @abstractmethod
    def visitRange(self,range):
        pass
    
    @abstractmethod
    def visitAssign(self,assign):
        pass
    
    @abstractmethod
    def visitExpression(self,expression):
        pass
    
    @abstractmethod
    def visitOrExp(self,or_exp):
        pass
    
    @abstractmethod
    def visitCompExp(self,comp_exp):
        pass
    
    @abstractmethod
    def visitCompOp(self,comp_op):
        pass
    
    @abstractmethod
    def visitOpArithmetic(self,op_arithmetic):
        pass
    
    @abstractmethod
    def visitFactor(self,factor):
        pass
    
    @abstractmethod
    def visitPower(self,power):
        pass
    
    @abstractmethod
    def visitTerm(self,term):
        pass
    
    @abstractmethod
    def visitArray(self,array):
        pass
    
    @abstractmethod
    def visitReturn(self,return):
         pass