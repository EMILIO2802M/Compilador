from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser
from GrammarLexer import GrammarLexer
from antlr4 import *

class MyVisitor(GrammarVisitor):
    def __init__(self):
      self.memory = {}

    #Definimos la asignacion 
    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value
    #Definimos la impresion
    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value
