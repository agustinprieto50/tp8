from repositorios import Repositorios


class ProductoService():

    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        new = (lastKey) + 1
        Repositorios.productosList[new] = producto.__dict__
        return new

    def delete_producto(self, num):
        if num not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        else:
            del Repositorios.productosList[num]

    def get_productosList(self):
        return Repositorios.productosList

    def update_producto(self, key, producto):
        if key not in Repositorios.productosList:
            raise ValueError("El producto no existe")
        Repositorios.productosList.update({key: producto.__dict__})

    def insertion_sort_precio(self, lista, tipo_orden):
        if tipo_orden == str("ascendente"):
            largo_indice = range(1, len(lista))
            for i in largo_indice:
                sort = lista[i]

                while i > 0 and lista[i-1]["_precio"] > sort["_precio"]:
                    lista[i], lista[i-1] = lista[i-1], lista[i]
                    i = i-1

            return lista

        if tipo_orden == str("descendente"):
            largo_indice = range(0, len(lista))
            for i in largo_indice:
                sort = lista[i]

                while i > 0 and lista[i-1]["_precio"] < sort["_precio"]:
                    lista[i], lista[i-1] = lista[i-1], lista[i]
                    i = i-1

            return lista

    def busqueda_binaria(self, repo, precio):
        repo_ordenado = self.insertion_sort_precio(repo, "ascendente")
        left = 0
        right = len(repo_ordenado) - 1

        while left <= right:
            mid = int((left + right)/2)

            if repo_ordenado[mid]["_precio"] == precio:
                return repo_ordenado[mid]

            if repo_ordenado[mid]["_precio"] > precio:
                right = mid - 1

            if repo_ordenado[mid]["_precio"] < precio:
                left = mid + 1

    def get_lista_estado(self, lista):
        repositorio = dict()
        for i in lista:
            if lista[i]['_estado'] == 'disponible':
                repositorio[i] = lista[i]
        return repositorio
