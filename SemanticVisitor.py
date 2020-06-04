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
        program.id.accept(self)
        program.body.accept(self)

    def visitProgramDecl(self,program__decl):
        program__decl.id.accept(self)
        program__decl.body.accept(self)
        program__decl.decl.accept(self)


    def visitSubprogram(self,subprogram):
        params = {}
        if subprogram.decl_param is not None:
            params = subprogram.decl_param.accept(self)
            st.addFunction(subprogram.id,params,subprogram.decl_param.type)
        else:
            st.addFunction(subprogram.id, params, subprogram.decl_param.type)
        st.beginScope(subprogram.id)
        for i in range(0, len(params), 2):
            st.addVar(params[i], params[i+1])


    def visitBody(self,body):
        body.cmd_loop.accept(self)
        body.id.accept(self)

    def visitDecl(self,decl):
        decl.var.accept(self)

    def visitDeclVarDecl(self,decl):
        decl.var.accept(self)
        decl.decl.accept(self)

    def visitVar(self,var):
        var.id.accept(self) # accept nos ids?

    def visitVarID(self,var):
        var.id1.accept(self)
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