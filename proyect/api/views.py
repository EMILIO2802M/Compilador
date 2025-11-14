from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.conf import settings
import logging
import json
import traceback

# Importamos nuestro metodo
from .utils import run_code

logger = logging.getLogger(__name__)


@api_view(['POST'])
def main(request):
    # Definimos el metodo de la peticion
    if request.method != 'POST':
        return JsonResponse({'code': ''}, status=405)

    try:
        # Parseamos el cuerpo de la peticion en un JSON
        body = request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse({'code': 'Json invalido'}, status=400)

    # Del Json obtenemos el que tenga 'text'
    code = data.get('text', '')

    try:
        # Ejecutamos las instrucciones con el metodo que definimos
        output = run_code(code)

        # Si run_code devolvió un traceback (string que empieza con 'Traceback'),
        # tratamos como error y devolvemos 500. En DEBUG devolvemos el traceback completo.
        if isinstance(output, str) and output.strip().startswith('Traceback'):
            logger.error('Error ejecutando código:\n%s', output)
            if getattr(settings, 'DEBUG', False):
                return JsonResponse({'error': output}, status=500)
            else:
                return JsonResponse({'error': 'Error interno al ejecutar el código'}, status=500)

        # Respuesta normal
        return JsonResponse({'output': output})

    except Exception:
        tb = traceback.format_exc()
        logger.exception('Excepción no controlada en la vista main: %s', tb)
        if getattr(settings, 'DEBUG', False):
            return JsonResponse({'error': tb}, status=500)
        else:
            return JsonResponse({'error': 'Error al procesar la solicitud'}, status=500)
