class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        # Solo cambiamos el color si el nuevo color está en los colores permitidos
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color
        # Este cambio asegura que no se modifique el color si no está en la lista permitida


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        # Cambia el registro del motor
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        # Solo asignamos el nuevo tipo si es "electrico" o "gasolina"
        if nuevo_tipo in ["electrico", "gasolina"]:
            self.tipo = nuevo_tipo
        # Este cambio asegura que el tipo solo se cambie a "electrico" o "gasolina"


class Auto:
    cantidadCreados = 0  # Atributo de clase para contar los autos creados

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        # Aseguramos que la lista de asientos esté inicializada
        self.asientos = asientos if asientos is not None else []  
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        # Contamos solo los elementos que son instancias de Asiento en la lista de asientos
        return len([asiento for asiento in self.asientos if isinstance(asiento, Asiento)])

    def verificarIntegridad(self):
        # Verificamos que todos los registros (del auto, motor y asientos) sean iguales
        registros = [self.registro, self.motor.registro] + [
            asiento.registro for asiento in self.asientos if isinstance(asiento, Asiento)
        ]
        # Usamos `all()` para asegurar que todos los registros son iguales al del auto
        if all(r == self.registro for r in registros):
            return "Auto original"
        else:
            return "Las piezas no son originales"