#objetos
#Cuenta
class CuentaAhorros:
    contador_numero_cuentas = 0
    def __obtener_numero_cuenta():
        CuentaAhorros.contador_numero_cuentas += 1
        return CuentaAhorros.contador_numero_cuentas
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.__saldo = 0
        self.numero_cuenta = CuentaAhorros.__obtener_numero_cuenta()
    def __str__(self):
        return str(self.nombre)+" "+str(self.numero_cuenta)
    def __eq__(self, value): #Sobrecarga del operador ==
        if isinstance(value, CuentaAhorros):
            return self.numero_cuenta == value.numero_cuenta
        return False #No iguales
    def __repr__(self):
        return self.__str__()
    def consultar_saldo(self):
        return self.__saldo
    def consignar(self, monto:float):
        if monto > 0:
            self.__saldo += monto
            return True
        return False
    def retirar(self, monto:float):
        if monto > 0 and self.__saldo >= monto:
            self.__saldo -= monto
            return True
        return False

#Diseño Lista Enlazada Simple
#Clase Nodo Simple
class NodoSimple:
    #Constructor
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
    def __str__(self):
        return str(self.dato)
    def __repr__(self):
        return self.__str__()
    def __eq__(self, value):
        if isinstance(value, NodoSimple):
            return self.dato == value.dato
        return False
#Clase Lista Simple
class ListaSimple:
    #Constructor
    def __init__(self):
        self.__nodo_inicial = None
    #Verificar si la lista está vacía
    def esta_vacia(self):
        return self.__nodo_inicial == None
    #adicionar datos al inicio
    def adicionar_inicio(self, dato_nuevo):
        #Verificar si la lista está vacía
        if self.esta_vacia():
            #Se define el nuevo nodo como el nodo inicial y único nodo
            self.__nodo_inicial = NodoSimple(dato_nuevo)
        else:
            #Se crea el nuevo nodo a adicionar
            nodo_nuevo = NodoSimple(dato_nuevo)
            #Se asigna el siguiente del nuevo nodo como el nodo inicial actual
            nodo_nuevo.siguiente = self.__nodo_inicial
            #Se asigna el nuevo nodo como nodo inicial de la lista
            self.__nodo_inicial = nodo_nuevo
    #recorrer la lista como str en el resultado
    def __str__(self):
        #Inicializar variable acumuladora (concatenación)
        resultado = ""
        #Definir nodo cursor para desplazarse sobre la lista (el nodo inicial no se desplaza)
        nodo_actual = self.__nodo_inicial
        #Ciclo para visitar cada nodo de la lista
        while nodo_actual:
            #Concatenación en la variable resultado del contenido del nodo (str)
            resultado += "["+str(nodo_actual) + "],"
            #Desplazar el nodo cursor hacia la derecha para visitar el siguiente nodo
            nodo_actual = nodo_actual.siguiente
        resultado = resultado.rstrip(",")
        return resultado


