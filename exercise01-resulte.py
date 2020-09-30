"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya


cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono


"""
# creando la lista vacia
listaRegistro = []
clientes = 0
CantidadCompradores = float(input("Cantidad de compradores"))
CostosTotales = 0

while CantidadCompradores > clientes:
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    CostosTotales = costo + CostosTotales

    clientes += 1
    print(CostosTotales)
    # punto de programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    clientes += 1


for registro in listaRegistro:
    print(registro)
