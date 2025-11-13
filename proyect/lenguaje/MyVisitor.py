from .GrammarVisitor import GrammarVisitor
from .GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    # Definimos la memoria o el entorno
    def __init__(self):
        # Inicializa la memoria/entorno donde guardamos variables
        self.memory = {}

    # Definimos la asignacion
    def visitAssing(self,ctx:GrammarParser.AssingContext):
        # Se obtiene el tipo de la variable (int, string)
        var_type = ctx.type_().getText()
        # Se obtiene el id o nombre de la variable
        name=ctx.ID().getText()
        # Se obtiene el valor, ya sea un valor numerico o una expresion
        value=self.visit(ctx.expr())


        # Se almacena en memoria a partir del nombre y el valor
        # self.memory[name]=value

        # Validacion de tipos
        if var_type == 'int' and not isinstance(value, int):
            raise TypeError(f"Error en '{name}' ")
        
        if var_type == 'string' and not isinstance(value, str):
            raise TypeError(f"Error en '{name}' ")

        # Se almacena en memoria el valor y su tipo
        self.memory[name] = {'value': value, 'type': var_type}


    # Definimos la impresion
    def visitPrint(self,ctx:GrammarParser.PrintContext):
        # Definimos la expresion que se desea mostrar
        value=self.visit(ctx.expr())
        # Imprime el valor
        print(value)

    # Definimos las expresiones
    def visitExpr(self, ctx):
        # Busca si existen IDs
        if ctx.ID():
            # Obtiene del contexto el nombre de la variable
            name=ctx.ID().getText()
            # Si el nombre de la variable no esto, lanza un error
            if name not in self.memory:
                #raise NameError(f"Variable '{name}' no definida")
                # Si existe el nombre retorna la variable
                #return self.memory[name]
                
                raise NameError(f"Variable '{name}' no ha sido definida")
            # Si existe el nombre retorna su valor
            return self.memory[name]['value']
        
        # Busca si es un numero
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        # Busca si es un string
        elif ctx.STRING():
            # Retorna el texto dentro de las comillas
            text = ctx.STRING().getText()
            return text[1:-1]
        # Busca el operador
        elif ctx.op:
            # Visita y obtiene lado izquierdo
            left=self.visit(ctx.expr(0))
            # Visita y obtiene lado derecho
            right=self.visit(ctx.expr(1))
            # Evalua la operacion a realizar
            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                #Verifica la division de cero
                if right == 0:
                    raise ValueError("Division por cero")
                return left / right
        
