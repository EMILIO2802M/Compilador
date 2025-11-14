from antlr4 import *
from lenguaje.GrammarLexer import GrammarLexer
from lenguaje.GrammarParser import GrammarParser
from lenguaje.MyVisitor import MyVisitor
import traceback
import io
import sys

def run_code(code:str):
    input_stream = InputStream(code)
    lexer =  GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()

    # Capturan la salida
    old_stdout = sys.stdout
    buf = io.StringIO()
    sys.stdout = buf

    try:
        # Creamos un objeto de nuestro visitor
        visitor = MyVisitor()
        # Visitamos el arbol con nuestro visitor
        visitor.visit(tree)
        # Capturamos la salida
        output = buf.getvalue()
        # Retornamos la salida
        return output
    # Capturamos excepciones
    except Exception:
        tb = traceback.format_exc()
        return tb
    finally:
        sys.stdout = old_stdout
