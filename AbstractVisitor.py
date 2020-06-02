from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitProgram(self,program):
         pass
    
    @abstractmethod
    def visitProgramDecl(self,program):
         pass

    @abstractmethod
    def visitSubprogram(self,subprogram):
        pass

    @abstractmethod
    def visitSubprogramDecl(self,subprogram):
        pass

    @abstractmethod
    def visitBody(self,body):
        pass

    @abstractmethod
    def visitDecl(self,decl):
        pass

    @abstractmethod
    def visitDeclVar(self,decl):
        pass

    @abstractmethod
    def visitDeclVarDecl(self,decl):
        pass

    @abstractmethod
    def visitDeclSubprogram(self,decl):
        pass

    @abstractmethod
    def visitDeclSubprogramDecl(self,decl):
        pass

    @abstractmethod
    def visitVar(self,var):
        pass

    @abstractmethod
    def visitVar(self,var):
        pass

    @abstractmethod
    def visitVarID(self,var):
        pass

    @abstractmethod
    def visitVarVarLoop(self,var):
        pass

    @abstractmethod
    def visitVarArray(self,var):
        pass

    @abstractmethod
    def visitVarLoop(self,var_loop):
        pass

    @abstractmethod
    def visitVarLoopLoop(self,var_loop):
        pass

    @abstractmethod
    def visitDeclParam(self,decl_param):
        pass

    @abstractmethod
    def visitDeclParamReturn(self,decl_param):
        pass

    @abstractmethod
    def visitParam(self,param):
        pass

    @abstractmethod
    def visitParamParam(self,param):
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
    def visitParamPassParamPass(self,param_pass):
        pass

    @abstractmethod
    def visitCmd(self,cmd):
        pass

    @abstractmethod
    def visitCmdIfStatement(self,cmd):
        pass

    @abstractmethod
    def visitCmdRepeatStatement(self,cmd):
        pass

    @abstractmethod
    def visitCmdPuts(self,cmd):
        pass

    @abstractmethod
    def visitCmdReturn(self,cmd):
        pass

    @abstractmethod
    def visitCmdAssign(self,cmd):
        pass

    @abstractmethod
    def visitCmdFunctionCall(self,cmd):
        pass

    @abstractmethod
    def visitCmdLoop(self,cmd_loop):
        pass

    @abstractmethod
    def visitCmdLoopLoop(self,cmd_loop):
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
    def visitIfStatementLoopElsif(self,if_statement_loop):
        pass

    @abstractmethod
    def visitIfStatementLoopElse(self,if_statement_loop):
        pass

    @abstractmethod
    def visitIfStatementLoopEnd(self,if_statement_loop):
        pass

    @abstractmethod
    def visitRepeatStatement(self,repeat_statement):
        pass

    @abstractmethod
    def visitRepeatStatementLoop(self,repeat_statement):
        pass

    @abstractmethod
    def visitRepeatStatementFor(self,repeat_statement):
        pass

    @abstractmethod
    def visitRepeatStatementWhile(self,repeat_statement):
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
    def visitExpressionAnd(self,expression):
        pass

    @abstractmethod
    def visitOrExp(self,or_exp):
        pass

    @abstractmethod
    def visitOrExpOr(self,or_exp):
        pass
    
    @abstractmethod
    def visitCompExp(self,comp_exp):
        pass

    @abstractmethod
    def visitCompExpOpArithmetic(self,comp_exp):
        pass

    @abstractmethod
    def visitCompOpGT(self,comp_op):
        pass

    @abstractmethod
    def visitCompOpGTE(self,comp_op):
        pass

    @abstractmethod
    def visitCompOpLT(self, comp_op):
        pass

    @abstractmethod
    def visitCompOpLTE(self, comp_op):
        pass

    @abstractmethod
    def visitCompOpNE(self, comp_op):
        pass

    @abstractmethod
    def visitCompOpE(self, comp_op):
        pass

    @abstractmethod
    def visitOpArithmeticPLUS(self,op_arithmetic):
        pass

    @abstractmethod
    def visitOpArithmeticMINUS(self,op_arithmetic):
        pass

    @abstractmethod
    def visitOpArithmeticFactor(self,op_arithmetic):
        pass
    
    @abstractmethod
    def visitFactorTIMES(self,factor):
        pass

    @abstractmethod
    def visitFactorDIVIDE(self,factor):
        pass

    @abstractmethod
    def visitFactorDPower(self,factor):
        pass

    @abstractmethod
    def visitPower(self,power):
        pass

    @abstractmethod
    def visitPowerUnary(self,power):
        pass

    @abstractmethod
    def visitUnary(self,unary):
        pass

    @abstractmethod
    def visitUnaryPLUS(self,unary):
        pass

    @abstractmethod
    def visitUnaryMINUS(self,unary):
        pass

    @abstractmethod
    def visitTermID(self,term):
        pass

    @abstractmethod
    def visitTermFunctionCall(self,term):
        pass

    @abstractmethod
    def visitTermExpression(self,term):
        pass

    @abstractmethod
    def visitArray(self,array):
        pass
    
    @abstractmethod
    def visitReturn(self,retorno):
         pass