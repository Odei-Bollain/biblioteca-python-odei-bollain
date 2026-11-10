
def listar_libro():
    tabla = []
    with open("datos/libros.txt", "r", encoding="utf-8") as f:
        for line in f:
            codigoL, titulo, autor, año, categoria  = line.strip().split(",")
            codigoL = str(codigoL)
            titulo = str(titulo)
            autor = str(autor)
            año = int(año)
            categoria = str(categoria)
    for fila in tabla:
        print(fila)
    return tabla