from AbstractVisitor import AbstractVisitor

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):

    def visitProgram(self,program):
        program.subprogam.accept(self)

    def visitProgramLoop(self,program):
        program.subprogam.accept(self)
        program.program.accept(self)


    def visitSubprogramFunction(self,subprogram):
        print(blank(),'function ',subprogram.id,end='',sep='')
        subprogram.decl_param.accept(self)
        print('is')
        subprogram.body.accept(self)

    def visitSubprogramProcedure(self,subprogram):
        print(blank(),'procedure ',subprogram.id,end='',sep='')
        subprogram.decl.accept(self)
        print('is')
        subprogram.body.accept(self)

    def visitSubprogramProcedureDecl(self,subprogram):
        print(blank(), 'procedure ', subprogram.id, end='', sep='')
        print('is')
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
        print(var.id,',',var.type,end='',sep='')

    def visitVarID(self,var):
        print (var.id1,',',var.type,':=',var.id2,end='',sep='')

    def visitVarVarLoop(self,var):
        var.var_loop.accept(self)
        print(var.id, ',', var.type, end='', sep='')

    def visitVarArray(self,var):
        var.array.accept(self)


    def visitVarLoop(self,var_loop):
        print(var_loop.id,',',end='', sep='')

    def visitVarLoopLoop(self,var_loop):
        var_loop.var_loop.accept(self)
        print(var_loop.id, ',',end = '', sep = '')


    def visitDeclParam(self,decl_param):
        print('(',end='', sep='')
        decl_param.param.accept(self)
        print(')', end='', sep='')

    def visitDeclParamReturn(self,decl_param):
        print('(',end='', sep='')
        decl_param.param.accept(self)
        print(')','return', decl_param.type,end='', sep='')


    def visitParam(self,param):
        print(param.id,':',param.type,';')

    def visitParamParam(self,param):
        print(param.id, ':', param.type, ';')
        param.param.accept(self)


    def visitFunctionCall(self,function_call):
        function_call.id.accept(self)
        function_call.param_pass.accept(self)


    def visitFunctionCallExp(self,function_call_exp):
        function_call_exp.id.accept(self)
        function_call_exp.param_pass.accept(self)


    def visitParamPass(self,param_pass):
        param_pass.expression.accept(self)

    def visitParamPassParamPass(self,param_pass):
        param_pass.expression.accept(self)
        param_pass.param_pass.accept(self)


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
        if_statement.expression.accept(self)
        if_statement.cmd_loop.accept(self)
        if_statement.if_statement_loop(self)


    def visitIfStatementLoopElsif(self,if_statement_loop):
        if_statement_loop.expression.accept(self)
        if_statement_loop.cmd_loop.accept(self)
        if_statement_loop.if_statement_loop(self)

    def visitIfStatementLoopElse(self,if_statement_loop):
        if_statement_loop.expression.accept(self)
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


    def visitExpression(self,expression):
        expression.op_exp.accept(self)

    def visitExpressionAnd(self,expression):
        expression.expression.accept(self)
        expression.or_exp.accept(self)


    def visitOrExp(self,or_exp):
        or_exp.comp_exp.accept(self)

    def visitOrExpOr(self,or_exp):
        or_exp.or_exp.accept(self)
        or_exp.comp_exp.accept(self)


    def visitCompExp(self,comp_exp):
        comp_exp.op_arithmetic.accept(self)

    def visitCompExpOpArithmetic(self,comp_exp):
        comp_exp.comp_op.accept(self)
        comp_exp.op_arithmetic.accept(self)
        comp_exp.comp_exp.accept(self)


    def visitCompOpGT(self,comp_op):
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
        op_arithmetic.op_arithmetic.accept(self)
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticMINUS(self,op_arithmetic):
        op_arithmetic.op_arithmetic.accept(self)
        op_arithmetic.factor.accept(self)

    def visitOpArithmeticFactor(self,op_arithmetic):
        op_arithmetic.factor.accept(self)


    def visitFactorTIMES(self,factor):
        factor.factor.accept(self)
        factor.power.accept(self)

    def visitFactorDIVIDE(self,factor):
        factor.factor.accept(self)
        factor.power.accept(self)

    def visitFactorPower(self,factor):
        factor.power.accept(self)


    def visitPower(self,power):
        power.power.accept(self)
        power.unary.accept(self)

    def visitPowerUnary(self,power):
        power.unary.accept(self)


    def visitUnaryPLUS(self,unary):
        unary.term.accept(self)

    def visitUnaryMINUS(self,unary):
        unary.term.accept(self)

    def visitUnary(self,unary):
        unary.term.accept(self)


    def visitTermID(self,term):
        term.id.accpet(self)

    def visitTermFunctionCall(self,term):
        term.function_call_exp.accept(self)

    def visitTermExpression(self,term):
        term.expression.accept(self)

    def visitArray(self,array):
        array.id.accept(self)
        array.range.accept(self)

    def visitReturn(self,retorno):
        retorno.expression.accept(self)

