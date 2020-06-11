from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import SintaxeAbstrata as sa


def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')


    def visitProgram(self,program):
        program.subprogram.accept(self)

    def visitProgramLoop(self,program):
        program.subprogram.accept(self)
        program.program.accept(self)


    def visitSubprogramFunction(self,subprogram):
        params = {}
        if subprogram.decl_param is not None:
            params = subprogram.decl_param.accept(self)
            st.addFunction(subprogram.id,params,subprogram.decl_param.type)
        else:
            st.addFunction(subprogram.id, params, subprogram.decl_param.type)
        st.beginScope(subprogram.id)
        for i in range(0, len(params), 2):
            st.addVar(params[i], params[i+1])
        subprogram.body.accept(self)

    def visitSubprogramProcedure(self,subprogram):
        st.beginScope(subprogram.id)
        subprogram.body.accept(self)


    def visitSubprogramProcedureDecl(self,subprogram):
        params = {}
        if subprogram.decl is not None:
            params = subprogram.decl.accept(self)
            st.addFunction(subprogram.id,params,subprogram.decl_param.type)
        else:
            st.addFunction(subprogram.id, params, subprogram.decl_param.type)
        st.beginScope(subprogram.id)
        for i in range(0, len(params), 2):
            st.addVar(params[i], params[i+1])
        subprogram.body.accept(self)

    def visitBody(self,body):
        body.cmd_loop.accept(self)
        body.id.accept(self)


    def visitDeclVar(self,decl): # como tratar declaração de veriável?
        decl.var.accept(self)

    def visitDeclVarDecl(self,decl):
        decl.var.accept(self)
        decl.decl.accept(self)


    def visitVar(self,var):
        var.id.accept(self) # accept nos ids?
        var.type.accept(self)
        st.addVar(var.id,var.type)

    def visitVarID(self,var):
        var.id1.accept(self)
        var.type.accept(self)
        st.addVar(var.id, var.type)
        var.id2.accept(self)

    def visitVarVarLoop(self,var):
        var.id.accept(self)
        var.var_loop.accept(self)

    def visitVarArray(self,var):
        var.array.accept(self)

    def visitVarLoop(self,var_loop):
        var_loop.id.accept(self)

    def visitVarLoopLoop(self,var_loop):
        var_loop.var_loop.accept(self)
        var_loop.id.accept(self)


    def visitDeclParam(self,decl_param):
        decl_param.param.accept(self)

    def visitDeclParamReturn(self,decl_param):
        decl_param.param.accept(self)


    def visitParam(self,param):
        return [param.id,param.type]

    def visitParamParam(self,param):
        return [param.id, param.type] + param.param.accept(type)


    def visitFunctionCall(self,function_call):
        bindable = st.getBindable(function_call.id)
        if bindable is not None and bindable[st.BINDABLE] == st.FUNCTION:
            typeParams = function_call.param_pass.accept(self)
            if list(bindable[st.PARAMS][1::2]) == typeParams:
                return bindable[st.TYPE]
            function_call.accept(self.printer)
            print("\n\t[Erro] Chamada de função inválida. Os tipos passados na chamada são:", typeParams)
            print('\tenquanto que os tipos definidos na função são:', bindable[st.PARAMS][1::2], '\n')
        else:
            function_call.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao inválida. A função", function_call.id,
                  "não existe, não foi definida ou foi definida após esta chamada\n")
        return None

    def visitFunctionCallEmpty(self,function_call):
        bindable = st.getBindable(function_call.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        function_call.accept(self.printer)
        print("\n\t[Erro] Chamada de funcao inválida. A função", function_call.id,
                  "não existe, não foi definida ou foi definida após esta chamada\n")
        return None


    def visitFunctionCallExp(self,function_call_exp):
        bindable = st.getBindable(function_call_exp.id)
        if bindable is not None and bindable[st.BINDABLE] == st.FUNCTION:
            typeParams = function_call_exp.param_pass.accept(self)
            if list(bindable[st.PARAMS][1::2]) == typeParams:
                return bindable[st.TYPE]
            function_call_exp.accept(self.printer)
            print("\n\t[Erro] Chamada de função inválida. Os tipos passados na chamada são:", typeParams)
            print('\tenquanto que os tipos definidos na função são:', bindable[st.PARAMS][1::2], '\n')
        else:
            function_call_exp.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao inválida. A função", function_call_exp.id,
                  "não existe, nao foi definida ou foi definida após esta chamada\n")

    def visitFunctionCallExpEmpty(self,function_call_exp):
        bindable = st.getBindable(function_call_exp.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        function_call_exp.accept(self.printer)
        print("\n\t[Erro] Chamada de funcao inválida. A função", function_call_exp.id,
                  "não existe, não foi definida ou foi definida após esta chamada\n")
        return None


    def visitParamPass(self,param_pass):
        return [param_pass.expression.accept(self)]

    def visitParamPassParamPass(self,param_pass):
        return [param_pass.expression.accept(self)] + param_pass.param_pass.accept(self)

    def visitCmdIfStatement(self,cmd):
        cmd.if_statement.accept(self)

    def visitCmdRepeatStatement(self,cmd):
        cmd.repeat_statement.accept(self)

    def visitCmdPuts(self,cmd):
        cmd.puts.accept(self)

    def visitCmdReturn(self,cmd):
        cmd.retorno.accept(self)

    def visitCmdAssign(self,cmd):
        cmd.assign.accept(self)

    def visitCmdFunctionCall(self,cmd):
        cmd.function_call.accept(self)


    def visitCmdLoop(self,cmd_loop):
        cmd_loop.cmd.accept(self)

    def visitCmdLoopLoop(self,cmd_loop):
        cmd_loop.cmd.accept(self)
        cmd_loop.cmd_loop.accept(self)


    def visitPuts(self,puts):
        puts.accept(self) #é um print. Não tem variável.


    def visitIfStatement(self,if_statement):
        type = if_statement.expression.accept(self)
        if type != st.BOOL:
            if_statement.expression.accept(self.printer)
            print("\n\t[Erro] A expressão ", end='')
            if_statement.expression.accept(self.printer)
            print(" é", type, end='')
            print(". Ela deve retornar boolean\n")
        if_statement.cmd_loop.accept(self)
        if_statement.if_statement_loop.accept(self)


    def visitIfStatementLoopElsif(self,if_statement_loop):
        type = if_statement_loop.expression.accept(self)
        if type != st.BOOL:
            if_statement_loop.expression.accept(self.printer)
            print("\n\t[Erro] A expressão ", end='')
            if_statement_loop.expression.accept(self.printer)
            print(" é", type, end='')
            print(". Ela deve retornar boolean\n")
        if_statement_loop.cmd_loop.accept(self)
        if_statement_loop.if_statement_loop(self)

    def visitIfStatementLoopElse(self,if_statement_loop):
        if_statement_loop.cmd_loop.accept(self)

    def visitIfStatementLoopEnd(self,if_statement_loop):
        if_statement_loop.accept(self) #é um end if. Não tem variável.

#---------------------------------------------------------------------------
    def visitRepeatStatementLoop(self,repeat_statement):
        repeat_statement.loop_statement.accept(self)

    def visitRepeatStatementFor(self,repeat_statement):
        repeat_statement.for_statement.accept(self)

    def visitRepeatStatementWhile(self,repeat_statement):
        repeat_statement.while_statement.accept(self)


    def visitLoopStatement(self,loop_statement):
        loop_statement.loop_statement.accept(self)


    def visitWhileStatement(self,while_statement):
        while_statement.expression.accept(self)
        while_statement.cmd_loop.accept(self)


    def visitForStatement(self,for_statement):
        for_statement.expression.accept(self)
        for_statement.cmd_loop.accept(self)


    def visitRange(self,range):
        range.id1.accept(self)
        range.id2.accept(self)


    def visitAssign(self,assign):
        assign.id.accept(self)
        assign.op_arithmetic.accept(self)


    def visitExpression(self,expression): #return
        expression.op_exp.accept(self)

    def visitExpressionAnd(self,expression): #return
        expression.expression.accept(self)
        expression.or_exp.accept(self)


    def visitOrExp(self,or_exp): #return
        or_exp.comp_exp.accept(self)

    def visitOrExpOr(self,or_exp): #return
        or_exp.or_exp.accept(self)
        or_exp.comp_exp.accept(self)


    def visitCompExp(self,comp_exp): #return
        comp_exp.op_arithmetic.accept(self)

    def visitCompExpOpArithmetic(self,comp_exp):
        comp_exp.comp_op.accept(self)
        comp_exp.op_arithmetic.accept(self)
        comp_exp.comp_exp.accept(self)


    def visitCompOpGT(self,comp_op): #return
        comp_op.accept(self)

    def visitCompOpGTE(self,comp_op): #return
        comp_op.accept(self)

    def visitCompOpLT(self,comp_op): #return
        comp_op.accept(self)

    def visitCompOpLTE(self,comp_op): #return
        comp_op.accept(self)

    def visitCompOpNE(self,comp_op): #return
        comp_op.accept(self)

    def visitCompOpE(self,comp_op): #return
        comp_op.accept(self)


    def visitOpArithmeticPLUS(self,op_arithmetic): #return
        op_arithmetic.op_arithmetic.accept(self)
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticMINUS(self,op_arithmetic): #return
        op_arithmetic.op_arithmetic.accept(self)
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticFactor(self,op_arithmetic): #return
        op_arithmetic.factor.accept(self)


    def visitFactorTIMES(self,factor): #return
        factor.factor.accept(self)
        factor.power.accept(self)

    def visitFactorDIVIDE(self,factor): #return
        factor.factor.accept(self)
        factor.power.accept(self)

    def visitFactorPower(self,factor): #return
        factor.power.accept(self)


    def visitPower(self,power): #return
        power.power.accept(self)
        power.unary.accept(self)

    def visitPowerUnary(self,power): #return
        power.unary.accept(self)


    def visitUnaryPLUS(self,unary): #return
        unary.term.accept(self)

    def visitUnaryMINUS(self,unary): #return
        unary.term.accept(self)

    def visitUnary(self,unary): #return
        unary.term.accept(self)


    def visitTermID(self,term): #return
        term.id.accpet(self)

    def visitTermFunctionCall(self,term): #return
        term.function_call_exp.accept(self)

    def visitTermExpression(self,term): #return
        term.expression.accept(self)

    def visitArray(self,array):
        array.id.accept(self)
        array.range.accept(self)

    def visitReturn(self,retorno):
        retorno.expression.accept(self)
