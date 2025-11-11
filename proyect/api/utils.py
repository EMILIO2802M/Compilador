from antlr4 import *
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
from lenguaje.MyVisitor import MyVisitor 

import io
import sys
def run_code(code: str):
    # Crear un flujo de entrada a partir del código fuente
    input_stream = InputStream(code)

    # Crear un lexer que tokeniza el flujo de entrada
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Crear un parser que construye el árbol de análisis sintáctico
    parser = GrammarParser(stream)
    tree = parser.program()

    # Capturan la salida
    old_stdout = sys.stdout()
    buf=io.StringIO()
    sys.stdout=buf

    # Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    # Visitamos el arbol con nuestro visitor
    visitor.visit(tree)

    # Capturamos la salida
    output=buf.getvalue()

    return output

