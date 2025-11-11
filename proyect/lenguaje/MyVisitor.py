from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser
from GrammarLexer import GrammarLexer
from antlr4 import *

class MyVisitor(GrammarVisitor):
    # Definimos la memoria o el entorno
    def __init__(self):
      self.memory = {}

    # Definimos la asignacion
    def visitAssign(self, ctx):
        # Se obtiene el id o nombre de la variable
        name = ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una operacion
        value = self.visit(ctx.expr())
        # Se alamacena en memoria a partir del nombre y el valor
        self.memory[name] = value
        return value
    #Definimos la impresion
    def visitPrint(self, ctx):
        # Definimos la expresion que se desea mostrar
        value = self.visit(ctx.expr())
        # Se imprime el valor
        print(value)
        return value
    # Definir las expresiones
    def visitExpr(self, ctx):
        # Busca si existe ID
        if ctx.ID():
            # Obtiene el nombre de la variable
            name = ctx.ID().getText()
            # Si el nombre de la variable no esta, lanza un error
            if name in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            # Si existe el nombre retorno, la variable
            return self.memory[name]
        # Busca el operador
        elif ctx.op:
            # Visita y obtiene lado izquierdo
            left = self.visit(ctx.expr(0))
            # Visita y obtiene lado derecho
            right = self.visit(ctx.expr(1))
            # Evalua la operacion a realizar
            if ctx.op.text == '+':
                return left + right
            if ctx.op.text == '-':
                return left - right
            if ctx.op.text == '*':
                return left * right
            if ctx.op.text == '/':
                # Verifica la division por cero
                if right == 0:
                    raise ZeroDivisionError("Division por cero")
                return left / right
        
