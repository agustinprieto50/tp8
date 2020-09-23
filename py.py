
from repositorios import Repositorios


def get_lista_estado(self, lista):
    repositorio = Repositorios.productosList
    for i in lista:
        if lista[i]['_estado'] == 'disponible':
            repositorio[i] = lista[i]
        return repositorio[i]

listita = {0: {'_descripcion': 'samsung s10', 
             '_precio': 200000, '_tipo': 'celular', '_estado': 'vendido'},
              1: {'_descripcion': 'samsung s20', '_precio': 400000,
              '_tipo': 'celular', '_estado': 'disponible'},
              2: {'_descripcion': 'lenovo t490', '_precio': 6000000,
              '_tipo': 'computadoras', '_estado': 'disponible'},
              3: {'_descripcion': 'HP', '_precio': 6000000,
              '_tipo': 'computadoras', '_estado': 'vendido'},
              4: {'_descripcion': 'acer', '_precio': 6000500,
              '_tipo': 'computadoras', '_estado': 'vendido'}}

get_lista_estado(listita)