def invetario_f():
    cantidad = int(input("Cantidad de productos: "))
    inventario = []

    for i in range(cantidad):
        codigo = input("codigo: ")
        nombre = input("nombre: ")
        precio = int(input("precio: "))
        stock = int(input("Stock: "))
        inventario.append({
            "codigo":codigo,
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }) 



    print(inventario)

    codigo = input("Ingrese el codigo del producto que desea consutlar: ")

    for i in range(len(inventario)):
        if codigo == inventario[i]["codigo"]:
            print(inventario[i])

        else:
            print("El codigo del productor no existe")


    

    codigo = input("Ingrese el codigo del producto que desea comprar: ")

    for i in range(len(inventario)):
        if(codigo == inventario[i]["codigo"]):
            inventario[i]["stock"] = inventario[i]["stock"] - 1

            print(inventario[i])
            break



invetario_f();
