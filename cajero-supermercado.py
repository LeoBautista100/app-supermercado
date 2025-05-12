#                    ***********APLICACION DE SUPERMERCADO***************
# ----------------------------------------------------------------------------------------

# Funcion para relizar una compra, devuelve un diccionario con producto y cantidad 

def entra_productos ():
    dato_compra = {}
    enterDetails = True
    while enterDetails:
        details = input ("Presione A para agregar un producto, Q para salir: ").lower()
        if details == 'a':
            producto = input("Ingrese el producto: ").lower()
            cantidad = int(input("Ingrese la cantidad: "))
            dato_compra.update({producto:cantidad})
        elif details == "q":
            enterDetails = False
        else:
            print("Ingrese una opcion correcta")
    return dato_compra

# Funcion que calcula el subtotal, recibe el producto y cantidad y calcula y retorna el subtotal de la compra

def getPrecio(producto, cantidad):
    precios = {
        'galletas': 3,
        'gaseosa': 5,
        'cerveza':8,
        'pan':2,
        'paty':10,
    }
    subtotal = precios[producto] * cantidad
    print(f"Producto: {producto} $ {precios[producto]} x {cantidad} = {subtotal}")
    return subtotal

# Funcion que calcula y aplica el descuento por socio en base a la categoría

def get_descuento(monto, socio):
    descuebto = 0
    if monto >= 25:
        if socio == "oro":
            monto = monto * 0.80
            descuebto = 20
        elif socio == "plata":
            monto = monto * 0.90
            descuebto = 10
        elif socio == "bronce":
            monto = monto * 0.95
            descuebto = 5
        elif socio == "no":
            print("No se aplica descuento por no ser socio")
        print(f"{descuebto} % de descuento por categoria {socio} en la compra")
    else: 
        print("NO hay descuento por monto menor a $25")
    return monto

# Funcion que genera una compra

def genera_compra(dato_compra,socio):
    monto = 0
    for clave, valor in dato_compra.items():
        monto += getPrecio(clave, valor)
    print(f"El subtotal es: $ {monto}")
    monto = get_descuento(monto, socio)
    print(f"El monto final es: $ {monto} \nGracias por su compra, vuelva pronto!!!!!")


# Inicio la aplicacion
dato_compra = entra_productos()
socio = input("Ingrese categoria de socio: ").lower()
genera_compra(dato_compra, socio)