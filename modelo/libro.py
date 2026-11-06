from errores.error import DatosIncorrectos

class Libro:
    def __init__(self, codigoL, titulo, autor, año, categoria, cod_socio):
        self.codigoL = codigoL
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.categoria = categoria
        self.cod_socio = cod_socio

    def __str__(self):
        return f'Codigo del Libro: {self.codigoL}, Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Categoria: {self.categoria}'