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
        visitor.visitProgram(self)

class c_program__loop(a_program):
    def __init__(self,subprogram,program):
        self.subprogram = subprogram
        self.program = program

    def accept(self, visitor):
        visitor.visitProgramLoop(self)

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
        visitor.visitSubprogramFunction(self)

class c_subprogram__procedure(a_subprogram):
    def __init__(self,id,body):
        self.id = id
        self.body = body

    def accept(self, visitor):
        visitor.visitSubprogramProcedure(self)

class c_subprogram__procedure_decl(a_subprogram):
    def __init__(self,id,decl, body):
        self.id = id
        self.body = body
        self.decl = decl

    def accept(self, visitor):
        visitor.visitSubprogramProcedureDecl(self)

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
        visitor.visitBody(self)


# ------------------------------------------------

class a_decl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_decl__var(a_decl):
    def __init__(self, var):
        self.var = var

    def accept(self, visitor):
        visitor.visitDeclVar(self)


class c_decl__var_decl(a_decl):
    def __init__(self, var, decl):
        self.var = var
        self.decl = decl

    def accept(self, visitor):
        visitor.visitDeclVarDecl(self)

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
        visitor.visitVar(self)


class c_var__term(a_var):
    def __init__(self,id,type,term):
        self.id = id
        self.type = type
        self.term = term

    def accept(self, visitor):
        visitor.visitVarTerm(self)


class c_var__var_loop(a_var):
    def __init__(self, var_loop,id,type):
        self.var_loop = var_loop
        self.id = id
        self.type = type

    def accept(self, visitor):
        visitor.visitVarVarLoop(self)


class c_var__array(a_var):
    def __init__(self, array):
        self.array = array

    def accept(self, visitor):
        visitor.visitVarArray(self)


# ------------------------------------------------

class a_var_loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_var_loop(a_var_loop):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        visitor.visitVarLoop(self)


class c_var_loop__loop(a_var_loop):
    def __init__(self, var_loop,id):
        self.var_loop = var_loop
        self.id = id

    def accept(self, visitor):
        visitor.visitVarLoopLoop(self)

# ------------------------------------------------
class a_type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_type__bool(a_type):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitTypeBool(self)


class c_type__char(a_type):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitTypeChar(self)


class c_type__float(a_type):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitTypeFloat(self)


class c_type__integer(a_type):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitTypeInteger(self)


class c_type__string(a_type):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitTypeString(self)

# ------------------------------------------------

class a_decl_param(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_decl_param(a_decl_param):
    def __init__(self, param):
        self.param = param

    def accept(self, visitor):
        visitor.visitDeclParam(self)


class c_decl_param__return(a_decl_param):
    def __init__(self, param,type):
        self.param = param
        self.type = type

    def accept(self, visitor):
        visitor.visitDeclParamReturn(self)


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
        visitor.visitParam(self)


class c_param__param(a_param):
    def __init__(self, id, type, param):
        self.param = param
        self.id = id
        self.type = type

    def accept(self, visitor):
        visitor.visitParamParam(self)


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
        visitor.visitFunctionCall(self)

class c_function_call_empty(a_function_call):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        visitor.visitFunctionCallEmpty(self)


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
        visitor.visitFunctionCallExp(self)

class c_function_call_exp_empty(a_function_call_exp):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        visitor.visitFunctionCallEmpty(self)


# -----------------------------------------------

class a_param_pass(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_param_pass(a_param_pass):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visitParamPass(self)


class c_param_pass__param_pass(a_param_pass):
    def __init__(self, expression, param_pass):
        self.expression = expression
        self.param_pass = param_pass

    def accept(self, visitor):
        visitor.visitParamPassParamPass(self)


# -----------------------------------------------

class a_cmd(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_cmd__if_statement(a_cmd):
    def __init__(self, if_statement):
        self.if_statement = if_statement

    def accept(self, visitor):
        visitor.visitCmdIfStatement(self)


class c_cmd__repeat_statement(a_cmd):
    def __init__(self, repeat_statement):
        self.repeat_statement = repeat_statement

    def accept(self, visitor):
        visitor.visitCmdRepeatStatement(self)


class c_cmd__puts(a_cmd):
    def __init__(self, puts):
        self.puts = puts

    def accept(self, visitor):
        visitor.visitCmdPuts(self)


class c_cmd__return(a_cmd):
    def __init__(self, retorno):
        self.retorno = retorno

    def accept(self, visitor):
        visitor.visitCmdReturn(self)


class c_cmd__assign(a_cmd):
    def __init__(self, assign):
        self.assign = assign

    def accept(self, visitor):
        visitor.visitCmdAssign(self)


class c_cmd__function_call(a_cmd):
    def __init__(self, function_call):
        self.function_call = function_call

    def accept(self, visitor):
        visitor.visitCmdFunctionCall(self)


# -----------------------------------------------

class a_cmd_loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_cmd_loop(a_cmd_loop):
    def __init__(self, cmd):
        self.cmd = cmd

    def accept(self, visitor):
        visitor.visitCmdLoop(self)


class c_cmd_loop__loop(a_cmd_loop):
    def __init__(self, cmd, cmd_loop):
        self.cmd = cmd
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        visitor.visitCmdLoopLoop(self)


# -----------------------------------------------

class a_puts(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_puts(a_puts):
    def __init__(self,string):
        self.string = string

    def accept(self, visitor):
        visitor.visitCmdPuts(self)


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
        visitor.visitIfStatement(self)


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
        visitor.visitIfStatementLoopElsif(self)


class c_if_statement_loop__else(a_if_statement_loop):
    def __init__(self, cmd_loop):
        self.cmd_loop = cmd_loop

    def accept(self, visitor):
        visitor.visitIfStatementLoopElse(self)


class c_if_statement_loop__end(a_if_statement_loop):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitIfStatementLoopEnd(self)


# -----------------------------------------------

class a_repeat_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_repeat_statement__loop(a_repeat_statement):
    def __init__(self, loop_statement):
        self.loop_statement = loop_statement

    def accept(self, visitor):
        visitor.visitRepeatStatementLoop(self)


class c_repeat_statement__for(a_repeat_statement):
    def __init__(self, for_statement):
        self.for_statement = for_statement

    def accept(self, visitor):
        visitor.visitRepeatStatementFor(self)


class c_repeat_statement__while(a_repeat_statement):
    def __init__(self, while_statement):
        self.while_statement = while_statement

    def accept(self, visitor):
        visitor.visitWhileStatement(self)


# -----------------------------------------------

class a_loop_statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_loop_statement(a_loop_statement):
    def __init__(self, loop_statement):
        self.loop_statement = loop_statement

    def accept(self, visitor):
        visitor.visitLoopStatement(self)


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
        visitor.visitWhileStatement(self)


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
        visitor.visitForStatement(self)

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
        visitor.visitRange(self)


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
        visitor.visitAssign(self)


# -----------------------------------------------

class a_expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_expression(a_expression):
    def __init__(self, op_exp):
        self.op_exp = op_exp

    def accept(self, visitor):
        visitor.visitExpression(self)


class c_expression__and(a_expression):
    def __init__(self, expression, or_exp):
        self.expression = expression
        self.or_exp = or_exp

    def accept(self, visitor):
        visitor.visitExpressionAnd(self)


# -----------------------------------------------

class a_or_exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_or_exp(a_or_exp):
    def __init__(self, comp_exp):
        self.comp_exp = comp_exp

    def accept(self, visitor):
        visitor.visitOrExp(self)


class c_or_exp__or(a_or_exp):
    def __init__(self, or_exp, comp_exp):
        self.or_exp = or_exp
        self.comp_exp = comp_exp

    def accept(self, visitor):
        visitor.visitOrExpOr(self)


# -----------------------------------------------

class a_comp_exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_comp_exp(a_comp_exp):
    def __init__(self, op_arithmetic):
        self.op_arithmetic = op_arithmetic

    def accept(self, visitor):
        visitor.visitCompExp(self)


class c_comp_exp__op_arithmetic(a_comp_exp):
    def __init__(self, comp_op, op_arithmetic, comp_exp):
        self.comp_op = comp_op
        self.op_arithmetic = op_arithmetic
        self.comp_exp = comp_exp

    def accept(self, visitor):
        visitor.visitCompExpOpArithmetic(self)


# -----------------------------------------------

class a_comp_op(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_comp_op__GT(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpGT(self)

class c_comp_op__GTE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpGTE(self)


class c_comp_op__LT(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpLT(self)


class c_comp_op__LTE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpLTE(self)


class c_comp_op__NE(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpNE(self)


class c_comp_op__E(a_comp_op):
    def __init__(self):
        pass

    def accept(self, visitor):
        visitor.visitCompOpE(self)


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
        visitor.visitOpArithmeticPLUS(self)


class c_op_arithmetic__MINUS(a_op_arithmetic):
    def __init__(self, op_arithmetic, factor):
        self.op_arithmetic = op_arithmetic
        self.factor = factor

    def accept(self, visitor):
        visitor.visitOpArithmeticMINUS(self)


class c_op_arithmetic__factor(a_op_arithmetic):
    def __init__(self, factor):
        self.factor = factor

    def accept(self, visitor):
        visitor.visitOpArithmeticFactor(self)


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
        visitor.visitFactorTIMES(self)


class c_factor__DIVIDE(a_factor):
    def __init__(self, factor, power):
        self.factor = factor
        self.power = power

    def accept(self, visitor):
        visitor.visitFactorDIVIDE(self)


class c_factor__power(a_factor):
    def __init__(self, power):
        self.power = power

    def accept(self, visitor):
        visitor.visitFactorPower(self)


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
        visitor.visitPower(self)


class c_power__unary(a_power):
    def __init__(self, unary):
        self.unary = unary

    def accept(self, visitor):
        visitor.visitPowerUnary(self)


# -----------------------------------------------

class a_unary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_unary__PLUS(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        visitor.visitUnaryPLUS(self)


class c_unary__MINUS(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        visitor.visitUnaryMINUS(self)


class c_unary(a_unary):
    def __init__(self, term):
        self.term = term

    def accept(self, visitor):
        visitor.visitUnary(self)


# -----------------------------------------------

class a_term(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_term__ID(a_term):
    def __init__(self,id):
        self.id = id

    def accept(self, visitor):
        visitor.visitTermID(self)


class c_term__function_call(a_term):
    def __init__(self, function_call_exp):
        self.function_call_exp = function_call_exp

    def accept(self, visitor):
        visitor.visitTermFunctionCall(self)


class c_term__expression(a_term):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visitTermExpression(self)

class c_term__literal(a_term):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        visitor.visitTermLiteral(self)

# -----------------------------------------------
class a_literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_literal_char(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralChar(self)


class c_literal_int(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralInt(self)

class c_literal_float(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralFloat(self)

class c_literal_str(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralStr(self)

class c_literal_true(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralTrue(self)

class c_literal_false(a_literal):
    def __init__(self,value):
        self.value = value

    def accept(self, visitor):
        visitor.visitLiteralFalse(self)

# -----------------------------------------------

class a_array(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_array(a_array):
    def __init__(self,id,range,type):
        self.id = id
        self.range = range
        self.type = type

    def accept(self, visitor):
        visitor.visitArray(self)


# -----------------------------------------------

class a_return(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class c_return(a_return):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        visitor.visitReturn(self)
