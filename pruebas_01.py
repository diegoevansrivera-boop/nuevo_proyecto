#Pruebas
from objetos import CuentaAhorros
from objetos import ListaSimple
#Cuentas
cuenta01 = CuentaAhorros("A")
cuenta02 = CuentaAhorros("B")
cuenta03 = CuentaAhorros("C")
#Consignar
cuenta01.consignar(500000)
cuenta02.consignar(10000)
cuenta03.consignar(123456)
#Lista Simple
lista_prueba = ListaSimple()
#Adicionar datos al inicio
lista_prueba.adicionar_inicio(cuenta03)
lista_prueba.adicionar_inicio(cuenta02)
lista_prueba.adicionar_inicio(cuenta01)
#Visualización de la lista en str
print(lista_prueba)
