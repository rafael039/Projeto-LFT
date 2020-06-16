from AbstractVisitor import AbstractVisitor
#from gramAbstrata import *
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):

    def visitProgram(self,program):
        program.subprogram.accept(self)

    def visitProgramLoop(self,program):
        program.subprogram.accept(self)
        program.program.accept(self)



    def visitSubprogramFunction(self,subprogram):
        print(blank(),'function ',subprogram.id,end='',sep='')
        print(' is')
        subprogram.decl_param.accept(self)
        subprogram.body.accept(self)

    def visitSubprogramProcedure(self,subprogram):
        print(blank(),'procedure ',subprogram.id,end='',sep='')
        print(' is')
        subprogram.body.accept(self)

    def visitSubprogramProcedureDecl(self,subprogram):
        print(blank(), 'procedure ', subprogram.id, end='', sep='')
        print(' is')
        subprogram.decl.accept(self)
        subprogram.body.accept(self)


    def visitBody(self,body):
        global tab
        print ('begin')
        tab =  tab + 3
        if body.cmd_loop != None:
            body.cmd_loop.accept(self)
        tab =  tab - 3
        print (blank(), 'end ',body.id, sep='')


    def visitDeclVar(self,decl):
        decl.var.accept(self)
        print(';')

    def visitDeclVarDecl(self,decl):
        decl.var.accept(self)
        print(';')
        decl.decl.accept(self)


    def visitVar(self,var):
        print(var.id,',',end='',sep='')
        var.type.accept(self)


    def visitVarTerm(self,var):
        print (var.id,',',end='',sep='')
        var.type.accept(self)
        print(' := ',end='',sep='')
        var.term.accept(self)

    def visitVarVarLoop(self,var):
        var.var_loop.accept(self)
        print(var.id, ',', end='', sep='')
        var.type.accept(self)

    def visitVarArray(self,var):
        var.array.accept(self)


    def visitVarLoop(self,var_loop):
        print(var_loop.id,',',end='', sep='')

    def visitVarLoopLoop(self,var_loop):
        var_loop.var_loop.accept(self)
        print(var_loop.id, ',',end = '', sep = '')

    def visitTypeBoolean(self, type): # como fazer?
        print(' Boolean',end = '')


    def visitTypeCharacter(self, type):
        print(' Character',end = '')


    def visitTypeFloat(self, type):
        print(' Float',end = '')


    def visitTypeInteger(self, type):
        print(' Integer',end = '')


    def visitTypeString(self, type):
        print(' String',end = '')


    def visitDeclParam(self,decl_param):
        print('(',end='', sep='')
        decl_param.param.accept(self)
        print(')', end='', sep='')

    def visitDeclParamReturn(self,decl_param):
        print('(',end='', sep='')
        decl_param.param.accept(self)
        print(')','return',end='', sep='')
        decl_param.type.accept(self)


    def visitParam(self,param):
        print(param.id,':',end='', sep='')
        param.type.accept(self)
        print(';')

    def visitParamParam(self,param):
        print(param.id,':',end='', sep='')
        param.type.accept(self)


    def visitFunctionCall(self,function_call):
        print(function_call.id,'(',end='', sep='')
        function_call.param_pass.accept(self)
        print(');')

    def visitFunctionCallEmpty(self, function_call):
        print(function_call.id,'(',end='', sep='')
        print(')',';',end='', sep='')

    def visitFunctionCallExp(self,function_call_exp):
        print(function_call_exp.id,'(',end='', sep='')
        function_call_exp.param_pass.accept(self)
        print(')',end='',sep='')

    def visitFunctionCallExpEmpty(self,function_call_exp):
        print(function_call_exp.id,'(',')', sep='')


    def visitParamPass(self,param_pass):
        param_pass.expression.accept(self)


    def visitParamPassParamPass(self,param_pass):
        param_pass.expression.accept(self)
        print(',',end='', sep='')
        param_pass.param_pass.accept(self)


    def visitCmdIfStatement(self,cmd):
        cmd.if_statement.accept(self)

    def visitCmdRepeatStatement(self,cmd):
        cmd.repeat_statement.accept(self)

    def visitCmdPuts(self,cmd):
        print('Puts(',end='', sep='')
        print(cmd.puts.string,end='', sep='')
        print(')')

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


    def visitPuts(self,puts): #Avaliar com o professor
        print('puts')
        puts.accept(self) #é um print. Não tem variável.


    def visitIfStatement(self,if_statement):
        print('if ', end='', sep='')
        if_statement.expression.accept(self)
        print('then')
        if_statement.cmd_loop.accept(self)
        if_statement.if_statement_loop.accept(self)


    def visitIfStatementLoopElsif(self,if_statement_loop):
        print('elsif ', sep='')
        if_statement_loop.expression.accept(self)
        if_statement_loop.cmd_loop.accept(self)
        if_statement_loop.if_statement_loop.accept(self)

    def visitIfStatementLoopElse(self,if_statement_loop):
        print('else ',sep='')
        if_statement_loop.cmd_loop.accept(self)
        print('end if;')

    def visitIfStatementLoopEnd(self,if_statement_loop):
        print('end if;')


    def visitRepeatStatementLoop(self,repeat_statement):
        repeat_statement.loop_statement.accept(self)

    def visitRepeatStatementFor(self,repeat_statement):
        repeat_statement.for_statement.accept(self)

    def visitRepeatStatementWhile(self,repeat_statement):
        repeat_statement.while_statement.accept(self)


    def visitLoopStatement(self,loop_statement):
        print('loop', sep='')
        loop_statement.loop_statement.accept(self)
        print('end loop;')


    def visitWhileStatement(self,while_statement):
        print('while ', end='', sep='')
        while_statement.while_statement.expression.accept(self) # while_statement da classe repeat, chama o atributo while_statement da classe c_while_statement
        print(' loop', sep='')
        while_statement.while_statement.cmd_loop.accept(self)
        print('end loop;')


    def visitForStatement(self,for_statement):
        print('for ', end='', sep='')
        print(for_statement.id, end='', sep='') #declarar variável
        print(' in ', end='', sep='')
        for_statement.range.accept(self)
        print(' loop', sep='')
        for_statement.cmd_loop.accept(self)
        print('end loop;')


    def visitRange(self,range):
        print(range.id1,'..',range.id2, sep='',end='')


    def visitAssign(self,assign):
        print(assign.id,':=', end='', sep='')
        assign.op_arithmetic.accept(self)
        print(';')


    def visitExpression(self,expression):
        expression.op_exp.accept(self)

    def visitExpressionAnd(self,expression):
        expression.expression.accept(self)
        print(' and ', end='')
        expression.or_exp.accept(self)


    def visitOrExp(self,or_exp):
        or_exp.comp_exp.accept(self)

    def visitOrExpOr(self,or_exp):
        or_exp.or_exp.accept(self)
        print(' or ', end='')
        or_exp.comp_exp.accept(self)


    def visitCompExp(self,comp_exp):
        comp_exp.op_arithmetic.accept(self)

    def visitCompExpOpArithmetic(self,comp_exp):
        comp_exp.comp_op.accept(self)
        comp_exp.op_arithmetic.accept(self)
        comp_exp.comp_exp.accept(self)


    def visitCompOpGT(self,comp_op):
        print(' > ',end='')

    def visitCompOpGTE(self,comp_op):
        print(' >= ',end='')

    def visitCompOpLT(self,comp_op):
        print(' < ',end='')

    def visitCompOpLTE(self,comp_op):
        print(' <= ',end='')

    def visitCompOpNE(self,comp_op):
        print(' != ',end='')

    def visitCompOpE(self,comp_op):
        print(' = ',end='')


    def visitOpArithmeticPLUS(self,op_arithmetic):
        op_arithmetic.op_arithmetic.accept(self)
        print(' + ', end='')
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticMINUS(self,op_arithmetic):
        op_arithmetic.op_arithmetic.accept(self)
        print(' - ', end='')
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticFactor(self,op_arithmetic):
        op_arithmetic.factor.accept(self)


    def visitFactorTIMES(self,factor):
        factor.factor.accept(self)
        print(' * ', end='')
        factor.power.accept(self)

    def visitFactorDIVIDE(self,factor):
        factor.factor.accept(self)
        print(' / ', end='')
        factor.power.accept(self)

    def visitFactorPower(self,factor):
        factor.power.accept(self)


    def visitPower(self,power):
        power.power.accept(self)
        print(' ** ', end='')
        power.unary.accept(self)

    def visitPowerUnary(self,power):
        power.unary.accept(self)


    def visitUnaryPLUS(self,unary):
        print('+', end='')
        unary.term.accept(self)

    def visitUnaryMINUS(self,unary):
        print('-', end='')
        unary.term.accept(self)

    def visitUnary(self,unary):
        unary.term.accept(self)


    def visitTermID(self,term):
        print(term.id,end='',sep='')

    def visitTermFunctionCall(self,term):
        term.function_call_exp.accept(self)


    def visitTermExpression(self,term):
        print('(', end='')
        term.expression.accept(self)
        print(')', end='')

    def visitTermLiteral(self, term):
        term.literal.accept(self)

    def visitLiteralChar(self,literal):
        print(literal.value,end='')

    def visitLiteralInt(self,literal):
        print(literal.value,end='')

    def visitLiteralFloat(self,literal):
        print(literal.value,end='')

    def visitLiteralStr(self,literal):
        print(literal.value,end='')

    def visitLiteralTrue(self,literal):
        print(literal.value,end='')

    def visitLiteralFalse(self,literal):
        print(literal.value,end='')

    def visitArray(self,array):
        print('type ',array.id,'is ','(',end='')
        array.range.accept(self)
        print(')',' of ',sep='',end='')
        array.type.accept(self)

    def visitReturn(self,retorno):
        print('return ',end='')
        retorno.expression.accept(self)
        print(';',end='')


