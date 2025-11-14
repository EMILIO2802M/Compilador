from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json

#Importamos nuestro metodo
from .utils import run_code

@api_view(['POST'])
def main(request):
    # Definimos el metodo de la peticion
    if request.method != 'POST':
        return JsonResponse(
            {'code':''},
             status = 405
        )

    try:
        # Parseamos el cuerpo de la petiición en un JSON
        body = request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse(
            {'code':'Json Invalido'}, 
            status = 405
        )
    
    # Del Json obtenemos el que tenga 'text
    code = data.get('text','') 
    # Ejecutamos las instrucciones con el metodo que definimos
    output = run_code(code)
    # Da una respuesta de tipo JSON
    return Response(
        {'output':output},
        status = status.HTTP_200_OK
    )    