import json
import re
import os

class Test:


    def __init__(self):
        try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
            if os.path.exists('db.json'):
                path='db.json'
            elif os.path.exists('/data/db.json'):
                path='/data/db.json'
            elif os.path.exists('./data/db.json'):
                path='./data/db.json'
            elif os.path.exists('../data/db.json'):
                path='../data/db.json'
            else:
                raise IOError("No se encuentra 'db.json'")
                
            with open(path) as data_file:
                self.datos = json.load(data_file)
        except IOError as fallo:
            print("Error {:s} leyendo db.json".format( fallo ) )

    def todos_datos(self):
        return self.datos

    def cuantos(self):
        return len(self.datos['datos'])

    def uno(self,dato_id):
        if dato_id > len(self.datos['datos']) or dato_id < 0:
            raise IndexError("Índice fuera de rango")
        return self.datos['datos'][dato_id]

    def nuevo( self, filename, course, date ):
        if ( not type(filename) is str):
            raise TypeError( "El nombre del fichero debe ser una cadena" )
        if ( not type(title) is str):
            raise TypeError( "El título del dato debe ser una cadena" )
        if not re.match("\d+/\d+\d+", date) :
            raise ValueError( "El formato de la fecha es incorrecto" )
        existe = list(filter( lambda dato: 'file' in dato and dato['file'] == filename, self.datos['datos'] ))
        if len(existe) > 0:
            raise ValueError( "Ese fichero ya existe")
        
        self.datos['datos'].append( {'file': filename,
                                     'course': course,
                                     'date': date } )
