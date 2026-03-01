#Pruebas
from objetos import CuentaAhorros
#Cuentas
cuenta01 = CuentaAhorros("A")
cuenta02 = CuentaAhorros("B")
cuenta03 = CuentaAhorros("C")
print(cuenta01)
print(cuenta02)
print(cuenta03)
lista_01 = [cuenta01, cuenta02, cuenta03]
print(lista_01)
#Consignar
cuenta01.consignar(500000)
cuenta02.consignar(10000)
cuenta03.consignar(123456)
for cuenta in lista_01:
    print(cuenta.nombre+" "+str(cuenta.consultar_saldo()))
#Retirar
cuenta01.retirar(10000)
cuenta02.retirar(5000)
cuenta03.retirar(100000)
for cuenta in lista_01:
    print(cuenta.nombre+" "+str(cuenta.consultar_saldo()))