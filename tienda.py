def ingresar_producto(productos):
    while True:
        codigo = input("Ingrese el código del producto (ej. P001): ")
        if codigo in productos:
            print(" Ese código ya existe. Ingrese un código único.")
        else:
            break

    nombre = input("Ingrese el nombre del producto: ")

    while True:
        categoria = input("Ingrese la categoría (Hombre/Mujer/Niño): ")
        if categoria in ["Hombre", "Mujer", "Niño"]:
            break
        else:
            print(" Categoría inválida. Intente con Hombre, Mujer o Niño.")

    while True:
        talla = input("Ingrese la talla (S, M, L, XL): ")
        if talla in ["S", "M", "L", "XL"]:
            break
        else:
            print(" Talla inválida. Intente con S, M, L o XL.")

    while True:
        try:
            precio = float(input("Ingrese el precio unitario (Q): "))
            if precio > 0:
                break
            else:
                print(" El precio debe ser mayor que Q0.00")
        except ValueError:
            print(" Ingrese un número válido.")

    while True:
        try:
            cantidad = int(input("ingrese cantidad de producto en stock "))
            if cantidad > 0:
                break
            else:
                print ("deve ingresar un numero entero positivo")

        except ValueError:
            print("has ingresado dato incorrecto")


    productos[codigo] = {
    "nombre": nombre,
    "categoria": categoria,
    "talla": talla,
    "precio": precio,
    "cantidad": cantidad
    }


def mostrar_productos(productos):
    print("\n Inventario completo:")

    for codigo, datos in productos.items():
        print(f"Código: {codigo}")
        print(f"  Nombre: {datos['nombre']}")
        print(f"  Categoría: {datos['categoria']}")
        print(f"  Talla: {datos['talla']}")
        print(f"  Precio: Q{datos['precio']:.2f}")
        print(f"  Cantidad: {datos['cantidad']}")

def buscar_productos(productos):
    codigo = int(input("ingrese el dodigo del producto que desea buscar: "))
    if codigo in productos:
        print(productos[codigo])
        producto = productos[codigo]
        print(f"  Nombre: {producto['nombre']}")
        print(f"  Categoría: {producto['categoria']}")
        print(f"  Talla: {producto['talla']}")
        print(f"  Precio: Q{producto['precio']:.2f}")
        print(f"  Cantidad en stock: {producto['cantidad']}")

    else:
        print("producto no existe")


productos = {}

try:
    n = int(input("¿Cuántos productos desea ingresar? "))
    for _ in range(n):
        print("\nIngrese los datos del producto:")
        ingresar_producto(productos)

    mostrar_productos(productos)
    buscar_productos(productos)


except ValueError:
    print(" Debe ingresar un número entero válido para la cantidad de productos.")