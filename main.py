#!/usr/bin/env python3

"""Datos del curso servidos para usted usando Hug"""

import os
import logging

import hug
from hug.middleware import LogMiddleware

from pythonjsonlogger import jsonlogger

from datetime import datetime

from Test.Test import Test

""" Define logger en formato JSON """
@hug.middleware_class()
class CustomLogger(LogMiddleware):
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        super().__init__(logger=logger)

    def _generate_combined_log(self, request, response):
        """Genera un log similar a nginx."""
        current_time = datetime.utcnow()
        return {'remote_addr':request.remote_addr,
                'time': current_time,
                'method': request.method,
                'uri': request.relative_uri,
                'status': response.status,
                'user-agent': request.user_agent }
    

""" Declara clase """ 
mis_datos = Test()

""" Define API REST """ 
@hug.get('/')
def status():
    """Devuelve estado"""
    return {"status":"ok"}

    """Devuelve estado"""
@hug.get('/status/')
def status2():
    return {"status":"ok"}
    """Devuelve todos los hitos"""
@hug.get('/todos/')
def status3():
    return mis_datos.todos_datos()

    """Devuelve un hito"""
@hug.get('/segun/{id}')
def funcion4(id:int):
    return mis_datos.uno(id)


""" Usa puerto del entorno si existe """ 
if 'PORT' in os.environ :
    port = int(os.environ['PORT'])
else:
    port = 8000

if __name__ == '__main__':
    hug.API(__name__).http.serve(port )
