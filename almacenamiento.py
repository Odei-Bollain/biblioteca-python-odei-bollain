
def listar_libro():
    tabla = []
    with open("datos/libros.txt", "r", encoding="utf-8") as f:
        for line in f:
            codigoL, titulo, autor, año, categoria  = line.strip().split("\n", 1)
            libro = [str(codigoL), str(titulo), str(autor), int(año), str(categoria)]
            tabla.append(libro)
        return tabla