from AbstractVisitor import AbstractVisitor

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitProgram(self,c_program):
        c_term__ID.id.accept(self)

