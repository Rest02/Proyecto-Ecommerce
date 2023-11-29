class Carro:
    def __init__(self, request):
        self.request = request # almacenamos la peticion actual como un atributo de la instancia
        self.session = request.session # almacenamos la session actual del usuario en un atributo de la instancia
        carro = self.session.get("carro") #Intenta obtener el diccionario del carro de la sesión. Si no existe, carro se establece en "None".
        if not carro:
            carro = self.session["carro"]={}  # Si carro no está, crea un diccionario vacio con la clave carro -  { carro : {} }              -  (clave : valor) -> {key : valor} -> {1: {precio:12990, cantidad:18, imagen : imagen}}
        #else:
        self.carro = carro # Si existe carro , agregado como atributo de la instancia



    def agregar(self, producto):  # metodo agregar
        if(str(producto.id) not in self.carro.keys()):  # Si la id del producto no esta en las claves del carro 
            self.carro[producto.id]={                   # Agregamos los datos a la clave del producto.id correspondiente
                "producto_id" : producto.id,
                "nombre_producto" : producto.nombre_producto,
                "precio_producto" : str(producto.precio_producto),
                "cantidad_disponible" : 1,
                "descripcion_producto" : producto.descripcion_producto
            }
        else:                                           # Si el producto cocn el producto.id esta en self.carro key hacemos lo siguiente
            for key, value in self.carro.items():       # iteramos el carro completo
                if key == str(producto.id):             # Si llegamos a encontrar una clave con el mismo valor de la id de nuestro producto
                    value["cantidad_disponible"] += 1              # Aumentamos el valor de la cantidad en 1
                    break                               # Rompemos el ciclo para que no siga buscando o recorriendo
        
        self.guardar_carro()                            # Guardamos llamando al metodo guardar_carro()



    def guardar_carro(self):    # metodo guardar carro 
        self.session["carro"] = self.carro              # El carro de la instancia , sera igual al de la session actual
        self.session.modified=True                      # Modificamos con iguala True


    def eliminar(self, producto):   # metodo eliminar producto
        producto.id = str(producto.id)                  # Almacenamos la id como string
        if producto.id in self.carro:                   # Si el producto esta en el carro
            del self.carro[producto.id]                 # Borra el producto con esa id del carro
            self.guardar_carro()                        # Guardamos llamando al metodo guardar_carro()

    def restar(self, producto): # metodo restar producto
        for key, value in self.carro.items():           # Recorremos por clave valor en los items del carro
            if key == str(producto.id):                 # Si llegamos a encontrar una clave con el mismo valor de la id de nuestro producto
                value["cantidad_disponible"] -= 1                 # Disminuimos el valor de la cantidad en 1
                if value["cantidad_disponible"] < 1:              # Si el valor de cantidad llega a 0
                    self.eliminar(producto)                               # Lo eliminamos llamando a la funcion eliminar
                    value["precio_producto"] = str(int(value["precio_producto"]) + producto.precio_producto)       
                break                                   # Rompemos el ciclo para que no siga buscando
        
        self.guardar_carro()                            # Guardamos llamando al metodo guardar_carro() 

    def limpiar_carro(self):    #metodo limpiar carro
        self.session["carro"]={}                        # Creamos nuevamente un diccionario de carro vacio siplemente en la session
        self.session.modified=True                      # Confirmamos los cambios de la session con modified = True