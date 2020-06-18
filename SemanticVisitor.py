from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from visitor import Visitor

import gramAbstrata as ga


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


    def visitDeclVar(self,decl):
        decl.var.accept(self)

    def visitDeclVarDecl(self,decl):
        decl.var.accept(self)
        decl.decl.accept(self)


    def visitVar(self,var):
        if isinstance(var.id, ga.c_term__ID):
            st.addVar(var.id, var.type)
            return var.type
        return None

    def visitVarTerm(self,var):
        typeVar = var.op_arithmetic.accept(self)
        if isinstance(var.id, ga.c_term__ID):
            st.addVar(var.id, typeVar)
            return typeVar
        return None

    def visitVarVarLoop(self,var):
        var.var_loop.accept(self)
        if isinstance(var.id, ga.c_term__ID):
            st.addVar(var.id, var.type)
            return var.type
        return None

    def visitVarArray(self,var):
        var.array.accept(self)

    def visitVarLoop(self,var_loop):
        var_loop.id.accept(self)

    def visitVarLoopLoop(self,var_loop):
        var_loop.var_loop.accept(self)
        var_loop.id.accept(self)


    def visitTypeBoolean(self, type): # como fazer?
        type.value = st.BOOL
        return type


    def visitTypeCharacter(self, type):
        type.value = st.CHAR
        return type


    def visitTypeFloat(self, type):
        type.value = st.FLOAT
        return type


    def visitTypeInteger(self, type):
        type.value = st.INT
        return type


    def visitTypeString(self, type):
        type.value = st.STR
        return type


    def visitDeclParam(self,decl_param):
        decl_param.param.accept(self)

    def visitDeclParamReturn(self,decl_param):
        decl_param.param.accept(self)


    def visitParam(self,param):
        return [param.id,param.type.value]

    def visitParamParam(self,param):
        return [param.id, param.type.value] + param.param.accept(self)


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


    def visitRepeatStatementLoop(self,repeat_statement):
        repeat_statement.loop_statement.accept(self)

    def visitRepeatStatementFor(self,repeat_statement):
        repeat_statement.for_statement.accept(self)

    def visitRepeatStatementWhile(self,repeat_statement):
        repeat_statement.while_statement.accept(self)


    def visitLoopStatement(self,loop_statement):
        loop_statement.loop_statement.accept(self)


    def visitWhileStatement(self,while_statement):
        type = while_statement.expression.accept(self)
        if type != st.BOOL:
            while_statement.expression.accept(self.printer)
            print("\n\t[Erro] A expressão ", end='')
            while_statement.expression.accept(self.printer)
            print(" é", type, end='')
            print(". Ela deve retornar boolean\n")
        while_statement.cmd_loop.accept(self)


    def visitForStatement(self,for_statement):
        type = for_statement.expression.accept(self)
        if type != st.BOOL:
            for_statement.expression.accept(self.printer)
            print("\n\t[Erro] A expressão ", end='')
            for_statement.expression.accept(self.printer)
            print(" é", type, end='')
            print(". Ela deve retornar boolean\n")
        for_statement.cmd_loop.accept(self)


    def visitRange(self,range): #como fazer?
        range.accept(self)


    def visitAssign(self,assign):
        typeVar = assign.op_arithmetic.accept(self)
        if isinstance(assign.id, ga.c_term__ID):
            st.addVar(assign.id, typeVar)
            return typeVar
        return None

    def visitExpression(self,expression):
        return expression.op_exp.accept(self)

    def visitExpressionAnd(self,expression):
        typeExp1 = expression.expression.accept(self)
        typeExp2 = expression.or_exp.accept(self)
        if typeExp1 is not st.BOOL | typeExp2 is not st.BOOL:
            expression.accept(self.printer)
            print('\n\t[Erro] Operação booleana inválida. A expressão ', end='')
            expression.expression.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            expression.or_exp.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return st.BOOL


    def visitOrExp(self,or_exp):
        return or_exp.comp_exp.accept(self)

    def visitOrExpOr(self,or_exp):
        typeExp1 = or_exp.or_exp.accept(self)
        typeExp2 = or_exp.comp_exp.accept(self)
        if typeExp1 is not st.BOOL | typeExp2 is not st.BOOL:
            or_exp.accept(self.printer)
            print('\n\t[Erro] Operação booleana inválida. A expressão ', end='')
            or_exp.or_exp.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            or_exp.comp_exp.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return st.BOOL


    def visitCompExp(self,comp_exp):
        return comp_exp.op_arithmetic.accept(self)

    def visitCompExpOpArithmetic(self,comp_exp):
        typeExp1 = comp_exp.comp_exp.accept(self)
        typeExp2 = comp_exp.comp_op.accept(self)

        if typeExp1 in st.Number | typeExp2 in st.Number:
            return st.BOOL
        comp_exp.accept(self.printer)
        print('\n\t[Erro] Comparação inválida. A expressão ', end='')
        comp_exp.comp_exp.accept(self.printer)
        print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
        comp_exp.comp_op.accept(self.printer)
        print(' é do tipo', typeExp2, '\n')
        return None


    def visitCompOpGT(self,comp_op): # como fazer?
        comp_op.accept(self)

    def visitCompOpGTE(self,comp_op):
        comp_op.accept(self)

    def visitCompOpLT(self,comp_op):
        comp_op.accept(self)

    def visitCompOpLTE(self,comp_op):
        comp_op.accept(self)

    def visitCompOpNE(self,comp_op):
        comp_op.accept(self)

    def visitCompOpE(self,comp_op):
        comp_op.accept(self)


    def visitOpArithmeticPLUS(self,op_arithmetic):
        typeExp1 = op_arithmetic.op_arithmetic.accept(self)
        typeExp2 = op_arithmetic.factor.accept(self)
        c = coercion(typeExp1,typeExp2)
        if c == None:
            op_arithmetic.accept(self.printer)
            print('\n\t[Erro] Soma inválida. A expressão ', end='')
            op_arithmetic.op_arithmetic.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            op_arithmetic.factor.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return c

    def visitOpArithmeticMINUS(self,op_arithmetic):
        typeExp1 = op_arithmetic.op_arithmetic.accept(self)
        typeExp2 = op_arithmetic.factor.accept(self)
        c = coercion(typeExp1,typeExp2)
        if c == None:
            op_arithmetic.accept(self.printer)
            print('\n\t[Erro] Subtração inválida. A expressão ', end='')
            op_arithmetic.op_arithmetic.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            op_arithmetic.factor.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return c


    def visitOpArithmeticFactor(self,op_arithmetic):
        return op_arithmetic.factor.accept(self)


    def visitFactorTIMES(self,factor):
        typeExp1 = factor.factor.accept(self)
        typeExp2 = factor.power.accept(self)
        c = coercion(typeExp1,typeExp2)
        if c == None:
            factor.accept(self.printer)
            print('\n\t[Erro] Multiplicação inválida. A expressão ', end='')
            factor.factor.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            factor.power.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return c

    def visitFactorDIVIDE(self,factor):
        typeExp1 = factor.factor.accept(self)
        typeExp2 = factor.power.accept(self)
        c = coercion(typeExp1,typeExp2)
        if c == None:
            factor.accept(self.printer)
            print('\n\t[Erro] Divisão inválida. A expressão ', end='')
            factor.factor.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            factor.power.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return c

    def visitFactorPower(self,factor):
        return factor.power.accept(self)


    def visitPower(self,power):
        typeExp1 = power.power.accept(self)
        typeExp2 = power.unary.accept(self)
        c = coercion(typeExp1,typeExp2)
        if c == None:
            power.accept(self.printer)
            print('\n\t[Erro] Potência inválida. A expressão ', end='')
            power.power.accept(self.printer)
            print(' é do tipo', typeExp1, 'enquanto a expressão ', end='')
            power.unary.accept(self.printer)
            print(' é do tipo', typeExp2, '\n')
            return None
        return c

    def visitPowerUnary(self,power):
        return power.unary.accept(self)


    def visitUnaryPLUS(self,unary):
        typeExp = unary.term.accept(self)
        if typeExp in st.Number:
            return typeExp
        unary.accept(self.printer)
        print('\n\t[Erro] Não é possivel fazer a opeação unária na expressão', end='')
        unary.term.accept(self.printer)
        return None

    def visitUnaryMINUS(self,unary):
        typeExp = unary.term.accept(self)
        if typeExp in st.Number:
            return typeExp
        unary.accept(self.printer)
        print('\n\t[Erro] Não é possivel fazer a opeação unária na expressão', end='')
        unary.term.accept(self.printer)
        return None

    def visitUnary(self,unary):
        return unary.term.accept(self)


    def visitTermID(self,term):
        idName = st.getBindable(term.id)
        if (idName != None):
            return idName[st.TYPE]
        return None

    def visitTermFunctionCall(self,term):
        return term.function_call_exp.accept(self)

    def visitTermExpression(self,term):
        return term.expression.accept(self)

    def visitTermLiteral(self, term):
        return term.literal.accept(self)


    def visitLiteralChar(self,literal): # como fazer
        return literal.value.accept(self)

    def visitLiteralInt(self,literal):
        return literal.value.accept(self)

    def visitLiteralFloat(self,literal):
        return literal.value.accept(self)

    def visitLiteralStr(self,literal):
        return literal.value.accept(self)

    def visitLiteralTrue(self,literal):
        return literal.value.accept(self)

    def visitLiteralFalse(self,literal):
        return literal.value.accept(self)


    def visitArray(self,array): # como fazer?
        array.id.accept(self)
        array.range.accept(self)

    def visitReturn(self,retorno):
        typeExp = retorno.expression.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (typeExp != bindable[st.TYPE]):
            retorno.accept(self.printer)
            print('\t[Erro] O retorno da funcao', scope, 'é do tipo', bindable[st.TYPE], end='')
            print(' no entanto, o retorno passado foi do tipo', typeExp, '\n')
        st.endScope()
