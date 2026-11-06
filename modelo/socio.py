from errores.error import DatosIncorrectos

class Socio:
    def __init__(self, codigoS, nombre, email, cod_libro):
        self.codigoS = codigoS
        self.nombre = nombre
        self.email = email
        self.cod_libro = cod_libro

    def __str__(self):
        return f'Codigo de socio: {self.codigoS} Nombre: {self.nombre}, Email: {self.email}'