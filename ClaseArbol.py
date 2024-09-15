from ClaseNodo import Nodo

class Arbol:
    __raiz__ = None # Puntero 
    __n__ = 0 #Cantidad de Nodos

    # Constructor
    def __init__(self):
        self.__raiz__ = None
        self.__n__ = 0

    # x = valor (100)
    def insertar(self, x):
        self.__raiz__ = self.__insertarMask(self.__raiz__, x)

    # Funcion (Me retorna el nuevo Arbol)
    def __insertarMask(self, nodoRaiz, x):
        if nodoRaiz is None: 
            return Nodo(x)
        else:
            if x < nodoRaiz.getData():
                nodoRaiz.setHijoIzquierdo(self.__insertarMask(nodoRaiz.getHijoIzquierdo(), x))
            else:
                nodoRaiz.setHijoDerecho(self.__insertarMask(nodoRaiz.getHijoDerecho(), x))
        return nodoRaiz

    # publico
    def cantidadNodos(self):
        return self.cantidadNodosR(self.__raiz__)
         
    def cantidadNodosR(self, nodoAux):
        if nodoAux is None:
            return 0
        else:
            return 1 + self.cantidadNodosR(nodoAux.getHijoIzquierdo()) + self.cantidadNodosR(nodoAux.getHijoDerecho())

    # def cantidadNodosPares(self):
    #     return self.cantidadNodosParesR(self.__raiz__)
    
    # def __cantidadNodosParesR(self, nodoAux):
    #     # en el caso que sea vacio el arbol
    #     if nodoAux is None:
    #         return 0
        
    #     # en el Caso que sea hoja
    #     if self.__eshoja(nodoAux):
    #         if nodoAux.getData() % 2 == 0:
    #             return 1
    #         else:
    #             return 0
            
    #     __cantidadNodosParesR(nodoAux.getHijoIzquierdo()) 
    #     __cantidadNodosParesR(nodoAux.getHijoDerecho())
        
    #             return 1 + self.__cantidadNodosParesR(nodoAux.getHijoIzquierdo()) + self.__cantidadNodosParesR(nodoAux.getHijoDerecho())
    #         else:
    #             return self.__cantidadNodosParesR(nodoAux.getHijoIzquierdo()) + self.__cantidadNodosParesR(nodoAux.getHijoDerecho())
   
   
    def __eshoja(self, nodo):
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None
    
    
    
    def inOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__inOrdenMask(self.__raiz__)
        print("---------------------------------------")

    def __inOrdenMask(self, nodo):
        if nodo is not None:
            self.__inOrdenMask(nodo.getHijoIzquierdo()) # Izquierdo
            print(nodo.getData())       # Padre
            self.__inOrdenMask(nodo.getHijoDerecho()) # Derecho

    def preOrden(self):
        if self.__raiz__ is None:
            print("El arbol esta Vacio")
        else:
            self.__preOrdenMask(self.__raiz__)

    def __preOrdenMask(self, nodo):  # Padre, Izquierdo, Derecho
        if nodo is not None:
            print(nodo.getData())  # Padre
            self.__preOrdenMask(nodo.getHijoIzquierdo())  # Izquierdo
            self.__preOrdenMask(nodo.getHijoDerecho())  # Derecho

    # Post Orden = Izquierdo, Derecho, Padre
    
    
    
    
    
    
    
    
    
    
    
    def obtenerAltura(self):
        return self.__obtenerAlturaRecursivo(self.__raiz__)
    
    def __obtenerAlturaRecursivo(self, nodoAux):
        if nodoAux is None:
            return 0
        # if self.__eshoja(self,nodoAux ) :
        #     return 1
        
        #Caso General
        cantI =  self.__obtenerAlturaRecursivo(nodoAux.getHijoIzquierdo()) # 3
        cantD =  self.__obtenerAlturaRecursivo(nodoAux.getHijoDerecho())  #4
        return max(cantI,cantD) + 1
            



    # Verificar Arbol Vacio
    def isVacio(self):
        if self.__raiz__ is None:
            print("El arbol esta vacio")
        else:
            print("El arbol no esta vacio")

    def isHoja(self, nodo):
        if nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None:
            print("El nodo es Hoja")
        else:
            print("El nodo no es hoja")

if __name__ == "__main__":
    arbol = Arbol()
    
    # Verificar Arbol Vacio
    arbol.insertar(100)
    arbol.insertar(80)
    arbol.insertar(90)
    arbol.insertar(75)
    # arbol.insertar(50)
    # arbol.insertar(30)
    
    arbol.inOrden()
    
    print('Cantidad Nodos:',arbol.cantidadNodos() ) 
    print('obtenerAltura: ', arbol.obtenerAltura())