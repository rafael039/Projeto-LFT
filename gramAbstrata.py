from abc import abstractmethod
from abc import ABCMeta
from visitor import Visitor

class a_program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_program(a_program):
    def __init__(self,subprogram):
        self.subprogram = subprogram

    def accept(self, visitor):
        Visitor.visitProgram(self,visitor)

class c_program__loop(a_program):
    def __init__(self,subprogram,program):
        self.subprogram = subprogram
        self.program = program

    def accept(self, visitor):
        Visitor.visitProgramLoop(self,visitor)

# ------------------------------------------------

class a_subprogram(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class c_subprogram__function(a_subprogram):
    def __init__(self,id,decl_param,body):
        self.id = id
        self.decl_param = decl_param
        self.body = body

    def accept(self, visitor):
        Visitor.visitSubprogramFunction(self,visitor)

class c_subprogram__procedure(a_subprogram):
    def __init__(self,id,body):
        self.id = id
        self.body = body

    def accept(self, visitor):
        Visitor.visitSubprogramProcedure(self,visitor)

class c_subprogram__procedure_decl(a_subprogram):
    def __init__(self,id,decl, body):
        self.id = id
        self.body = body
        self.decl = decl

    def accept(self, visitor):
        Visitor.visitSubprogramProcedureDecl(self, visitor)

# ------------------------------------------------

class a_body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_body(a_body):
    def __init__(self, cmd_loop,id):
        self.cmd_loop = cmd_loop
        self.id = id

    def accept(self, visitor):
        Visitor.visitBody(self,visitor)


# ------------------------------------------------

class a_decl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_decl__var(a_decl):
    def __init__(self, var):
        self.var = var

    def accept(self, visitor):
        Visitor.visitDeclVar(self,visitor)


class c_decl__var_decl(a_decl):
    def __init__(self, var, decl):
        self.var = var
        self.decl = decl

    def accept(self, visitor):
        Visitor.visitDeclVarDecl(self,visitor)

# ------------------------------------------------

class a_var(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_var(a_var):
    def __init__(self,id,type):
        self.id = id
        self.type = type


    def accept(self, visitor):
        Visitor.visitVar(self,visitor)


class c_var__term(a_var):
    def __init__(self,id,type,term):
        self.id = id
        self.type = type
        self.term = term

    def accept(self, visitor):
        Visitor.visitVarTerm(self,visitor)


class c_var__var_loop(a_var):
    def __init__(self, var_loop,id,type):
        self.var_loop = var_loop
        self.id = id
        self.type = type

    def accept(self, visitor):
        Visitor.visitVarVarLoop(self,visitor)


class c_var__array(a_var):
    def __init__(self, array):
        self.array = array

    def accept(self, visitor):
        Visitor.visitVarArray(self,visitor)


# ------------------------------------------------

class a_var_loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_var_loop(a_var_loop):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        Visitor.visitVarLoop(self,visitor)


class c_var_loop__loop(a_var_loop):
    def __init__(self, var_loop,id):
        self.var_loop = var_loop
        self.id = id

    def accept(self, visitor):
        Visitor.visitVarLoopLoop(self,visitor)

# ------------------------------------------------
class a_type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_type__bool(a_type):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitTypeBool(self,visitor)


class c_type__char(a_type):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitTypeChar(self, visitor)


class c_type__float(a_type):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitTypeFloat(self, visitor)


class c_type__integer(a_type):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitTypeInteger(self, visitor)


class c_type__string(a_type):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitTypeString(self, visitor)

# ------------------------------------------------

class a_decl_param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_decl_param(a_decl_param):
    def __init__(self, param):
        self.param = param

    def accept(self, visitor):
        Visitor.visitDeclParam(self,visitor)


class c_decl_param__return(a_decl_param):
    def __init__(self, param,type):
        self.param = param
        self.type = type

    def accept(self, visitor):
        Visitor.visitDeclParamReturn(self,visitor)


# -----------------------------------------------

class a_param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_param(a_param):
    def __init__(self,id,type):
        self.id = id
        self.type = type

    def accept(self, visitor):
        Visitor.visitParam(self,visitor)


class c_param__param(a_param):
    def __init__(self, id, param, type):
        self.param = param
        self.id = id
        self.type = type

    def accept(self, visitor):
        Visitor.visitParamParam(self,visitor)


# -----------------------------------------------

class a_function_call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_function_call(a_function_call):
    def __init__(self,id, param_pass):
        self.id = id
        self.param_pass = param_pass

    def accept(self, visitor):
        Visitor.visitFunctionCall(self,visitor)

class c_function_call_empty(a_function_call):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        Visitor.visitFunctionCallEmpty(self,visitor)


# -----------------------------------------------

class a_function_call_exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_function_call_exp(a_function_call_exp):
    def __init__(self, id,param_pass):
        self.id = id
        self.param_pass = param_pass

    def accept(self, visitor):
        Visitor.visitFunctionCallExp(self,visitor)

class c_function_call_exp_empty(a_function_call_exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        Visitor.visitFunctionCallEmpty(self,visitor)


# -----------------------------------------------

class a_param_pass(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_param_pass(a_param_pass):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        Visitor.visitParamPass(self,visitor)


class c_param_pass__param_pass(a_param_pass):
    def __init__(self, expression, param_pass):
        self.expression = expression
        self.param_pass = param_pass

    def accept(self, visitor):
        Visitor.visitParamPassParamPass(self,visitor)


# -----------------------------------------------

class a_cmd(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_cmd__if_statement(a_cmd):
    def __init__(self, if_statement):
        self.if_statement = if_statement

    def accept(self, visitor):
        Visitor.visitCmdIfStatement(self,visitor)


class c_cmd__repeat_statement(a_cmd):
    def __init__(self, repeat_statement):
        self.repeat_statement = repeat_statement

    def accept(self, visitor):
        Visitor.visitCmdRepeatStatement(self,visitor)


class c_cmd__puts(a_cmd):
    def __init__(self, puts):
        self.puts = puts

    def accept(self, visitor):
        Visitor.visitCmdPuts(self,visitor)


class c_cmd__return(a_cmd):
    def __init__(self, retorno):
        self.retorno = retorno

    def accept(self, visitor):
        Visitor.visitCmdReturn(self,visitor)


class c_cmd__assign(a_cmd):
    def __init__(self, assign):
        self.assign = assign

    def accept(self, visitor):
        Visitor.visitCmdAssign(self,visitor)


class c_cmd__function_call(a_cmd):
    def __init__(self, function_call):
        self.function_call = function_call

    def accept(self, visitor):
        Visitor.visitCmdFunctionCall(self,visitor)


# -----------------------------------------------

class a_cmd_loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_cmd_loop(a_cmd_loop):
    def __init__(self, cmd):
        self.cmd = cmd

    def accept(self, visitor):
        Visitor.visitCmdLoop(self,visitor)


class c_cmd_loop__loop(a_cmd_loop):
    def __init__(self, cmd, cmd_loop):
        self.cmd = cmd
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        Visitor.visitCmdLoopLoop(self,visitor)


# -----------------------------------------------

class a_puts(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_puts(a_puts):
    def __init__(self,string):
        self.string = string

    def accept(self, visitor):
        Visitor.visitCmdPuts(self,visitor)


# -----------------------------------------------

class a_if_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_if_statement(a_if_statement):
    def __init__(self, expression, cmd_loop, if_statement_loop):
        self.expression = expression
        self.cmd_loop = cmd_loop
        self.if_statement_loop = if_statement_loop

    def accept(self, visitor):
        Visitor.visitIfStatement(self,visitor)


# -----------------------------------------------

class a_if_statement_loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_if_statement_loop__elsif(a_if_statement_loop):
    def __init__(self, expression, cmd_loop, if_statement_loop):
        self.expression = expression
        self.cmd_loop = cmd_loop
        self.if_statement_loop = if_statement_loop

    def accept(self, visitor):
        Visitor.visitIfStatementLoopElsif(self,visitor)


class c_if_statement_loop__else(a_if_statement_loop):
    def __init__(self, expression, cmd_loop):
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        Visitor.visitIfStatementLoopElse(self,visitor)


class c_if_statement_loop__end(a_if_statement_loop):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitIfStatementLoopEnd(self,visitor)


# -----------------------------------------------

class a_repeat_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_repeat_statement__loop(a_repeat_statement):
    def __init__(self, loop_statement):
        self.loop_statement = loop_statement

    def accept(self, visitor):
        Visitor.visitRepeatStatementLoop(self,visitor)


class c_repeat_statement__for(a_repeat_statement):
    def __init__(self, for_statement):
        self.for_statement = for_statement

    def accept(self, visitor):
        Visitor.visitRepeatStatementFor(self,visitor)


class c_repeat_statement__while(a_repeat_statement):
    def __init__(self, while_statement):
        self.while_statement = while_statement

    def accept(self, visitor):
        Visitor.visitWhileStatement(self,visitor)


# -----------------------------------------------

class a_loop_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_loop_statement(a_loop_statement):
    def __init__(self, loop_statement):
        self.loop_statement = loop_statement

    def accept(self, visitor):
        Visitor.visitLoopStatement(self,visitor)


# -----------------------------------------------

class a_while_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_while_statement(a_while_statement):
    def __init__(self, expression, cmd_loop):
        self.expression = expression
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        Visitor.visitWhileStatement(self,visitor)


# -----------------------------------------------

class a_for_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_for_statement(a_for_statement):
    def __init__(self, id, range, cmd_loop):
        self.id = id
        self.range = range
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        Visitor.visitForStatement(self,visitor)

# -----------------------------------------------

class a_range(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_range(a_range):
    def __init__(self,id1,id2):
        self.id1 = id1
        self.id2 = id2

    def accept(self, visitor):
        Visitor.visitRange(self,visitor)


# -----------------------------------------------

class a_assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_assign(a_assign):
    def __init__(self, id, op_arithmetic):
        self.id = id
        self.op_arithmetic = op_arithmetic

    def accept(self, visitor):
        Visitor.visitAssign(self,visitor)


# -----------------------------------------------

class a_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_expression(a_expression):
    def __init__(self, op_exp):
        self.op_exp = op_exp

    def accept(self, visitor):
        Visitor.visitExpression(self,visitor)


class c_expression__and(a_expression):
    def __init__(self, expression, or_exp):
        self.expression = expression
        self.or_exp = or_exp

    def accept(self, visitor):
        Visitor.visitExpressionAnd(self,visitor)


# -----------------------------------------------

class a_or_exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_or_exp(a_or_exp):
    def __init__(self, comp_exp):
        self.comp_exp = comp_exp

    def accept(self, visitor):
        Visitor.visitOrExp(self,visitor)


class c_or_exp__or(a_or_exp):
    def __init__(self, or_exp, comp_exp):
        self.or_exp = or_exp
        self.comp_exp = comp_exp

    def accept(self, visitor):
        Visitor.visitOrExpOr(self,visitor)


# -----------------------------------------------

class a_comp_exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_comp_exp(a_comp_exp):
    def __init__(self, op_arithmetic):
        self.op_arithmetic = op_arithmetic

    def accept(self, visitor):
        Visitor.visitCompExp(self,visitor)


class c_comp_exp__op_arithmetic(a_comp_exp):
    def __init__(self, comp_op, op_arithmetic, comp_exp):
        self.comp_op = comp_op
        self.op_arithmetic = op_arithmetic
        self.comp_exp = comp_exp

    def accept(self, visitor):
        Visitor.visitCompExpOpArithmetic(self,visitor)


# -----------------------------------------------

class a_comp_op(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_comp_op__GT(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpGT(self,visitor)

class c_comp_op__GTE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpGTE(self,visitor)


class c_comp_op__LT(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpLT(self,visitor)


class c_comp_op__LTE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpLTE(self,visitor)


class c_comp_op__NE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpNE(self,visitor)


class c_comp_op__E(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        Visitor.visitCompOpE(self,visitor)


# -----------------------------------------------

class a_op_arithmetic(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_op_arithmetic__PLUS(a_op_arithmetic):
    def __init__(self, op_arithmetic, factor):
        self.op_arithmetic = op_arithmetic
        self.factor = factor

    def accept(self, visitor):
        Visitor.visitOpArithmeticPLUS(self,visitor)


class c_op_arithmetic__MINUS(a_op_arithmetic):
    def __init__(self, op_arithmetic, factor):
        self.op_arithmetic = op_arithmetic
        self.factor = factor

    def accept(self, visitor):
        Visitor.visitOpArithmeticMINUS(self,visitor)


class c_op_arithmetic__factor(a_op_arithmetic):
    def __init__(self, factor):
        self.factor = factor

    def accept(self, visitor):
        Visitor.visitOpArithmeticFactor(self,visitor)


# -----------------------------------------------

class a_factor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_factor__TIMES(a_factor):
    def __init__(self, factor, power):
        self.factor = factor
        self.power = power

    def accept(self, visitor):
        Visitor.visitFactorTIMES(self,visitor)


class c_factor__DIVIDE(a_factor):
    def __init__(self, factor, power):
        self.factor = factor
        self.power = power

    def accept(self, visitor):
        Visitor.visitFactorDIVIDE(self,visitor)


class c_factor__power(a_factor):
    def __init__(self, power):
        self.power = power

    def accept(self, visitor):
        Visitor.visitFactorPower(self,visitor)


# -----------------------------------------------

class a_power(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_power(a_power):
    def __init__(self, power, unary):
        self.power = power
        self.unary = unary

    def accept(self, visitor):
        Visitor.visitPower(self,visitor)


class c_power__unary(a_power):
    def __init__(self, unary):
        self.unary = unary

    def accept(self, visitor):
        Visitor.visitPowerUnary(self,visitor)


# -----------------------------------------------

class a_unary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_unary__PLUS(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        Visitor.visitUnaryPLUS(self,visitor)


class c_unary__MINUS(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        Visitor.visitUnaryMINUS(self,visitor)


class c_unary(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        Visitor.visitUnary(self,visitor)


# -----------------------------------------------

class a_term(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_term__ID(a_term):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        Visitor.visitTermID(self,visitor)


class c_term__function_call(a_term):
    def __init__(self, function_call_exp):
        self.function_call_exp = function_call_exp

    def accept(self, visitor):
        Visitor.visitTermFunctionCall(self,visitor)


class c_term__expression(a_term):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        Visitor.visitTermExpression(self,visitor)

class c_term__literal(a_term):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        Visitor.visitTermLiteral(self,visitor)

# -----------------------------------------------
class a_literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_literal_char(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralChar(self,visitor)


class c_literal_int(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralInt(self,visitor)

class c_literal_float(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralFloat(self,visitor)

class c_literal_str(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralStr(self,visitor)

class c_literal_true(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralTrue(self,visitor)

class c_literal_false(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        Visitor.visitLiteralFalse(self,visitor)

# -----------------------------------------------

class a_array(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_array(a_array):
    def __init__(self,type1,id,range,type2):
        self.type1 = type1
        self.id = id
        self.range = range
        self.type2 = type2

    def accept(self, visitor):
        Visitor.visitArray(self,visitor)


# -----------------------------------------------

class a_return(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_return(a_return):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        Visitor.visitReturn(self,visitor)
