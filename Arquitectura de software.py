class Producto:
    def obtener_precio(self):
        pass

class ProductoA(Producto):
    def obtener_precio(self):
        return 10.0

class ProductoB(Producto):
    def obtener_precio(self):
        return 20.0

class FabricaProducto:
    def crear_producto(self, tipo):
        if tipo == 'A':
            return ProductoA()
        elif tipo == 'B':
            return ProductoB()
        else:
            return None

# Patrón Estructural: Adapter
# Adaptador para integrar diferentes métodos de pago en el sistema.

class Pago:
    def realizar_pago(self, monto):
        pass

class PagoPayPal(Pago):
    def realizar_pago(self, monto):
        print(f"Pago de ${monto} realizado con PayPal.")

class PagoTarjeta(Pago):
    def realizar_pago(self, monto):
        print(f"Pago de ${monto} realizado con Tarjeta.")

class AdaptadorPago:
    def __init__(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def pagar(self, monto):
        self.metodo_pago.realizar_pago(monto)

# Patrón de Comportamiento: Observer
# Se utiliza para notificar cuando el inventario cambia.

class Observador:
    def actualizar(self, mensaje):
        pass

class Inventario(Observador):
    def actualizar(self, mensaje):
        print(f"Inventario actualizado: {mensaje}")

class SistemaVentas:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, obs):
        self.observadores.append(obs)

    def notificar(self, mensaje):
        for obs in self.observadores:
            obs.actualizar(mensaje)

    def vender(self, producto):
        print(f"Producto vendido: {producto}")
        self.notificar(f"Se vendió un {producto}")

# Ejemplo de uso
fabrica = FabricaProducto()
producto = fabrica.crear_producto('A')

pago = AdaptadorPago(PagoPayPal())
pago.pagar(producto.obtener_precio())

sistema = SistemaVentas()
inventario = Inventario()
sistema.agregar_observador(inventario)
sistema.vender("Producto A")
