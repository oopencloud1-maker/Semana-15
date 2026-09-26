# Programa para registrar productos de una tienda

# Diccionario para almacenar los productos
productos = {}

while True:
    print("\n--- REGISTRO DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar un producto
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")

        productos[nombre] = precio
        print("Producto agregado correctamente.")

    # Mostrar los productos
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\nProductos registrados:")
            for nombre, precio in productos.items():
                print("Producto:", nombre, "- Precio:", precio)

    # Buscar un producto
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto que desea buscar: ")

        if nombre in productos:
            print("Producto encontrado.")
            print("Producto:", nombre)
            print("Precio:", productos[nombre])
        else:
            print("El producto no existe.")

    # Salir del programa
    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")