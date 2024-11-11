class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio= precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        colores_permitidos =["rojo", "verde","amarillo","negro"]
        if nuevo_color in colores_permitidos:
            self.color=nuevo_color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros= numeroCilindros = numeroCilindros
        self.tipo =tipo
        self.registro=registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro=nuevo_registro

    def asignarTipo(self,nuevo_tipo):
        if nuevo_tipo in ["electrico","gasolina"]:
            self.tipo=nuevo_tipo

class Auto:
    cantidadCreados=0

    def __init__(self, modelo, precio, marca, motor, registro, asientos=[]):
        self.modelo=modelo
        self.precio=precio
        self.marca=marca
        self.registro=registro
        self.asientos=asientos
        Auto.cantidadCreados +=1

    def cantidadAsientos(self):
        return len([asiento for asiento in self.asientos if isinstance(asiento,Asiento)])
    
    def verificarIntegridad (self):
        registros = [self.registro, self.motor.registro] + [asiento.registro for asiento in self.asientos]
        if all(r==self.registro for r in registros):
            return "Auto original"
        else:
            return "Las piezas no son originales"