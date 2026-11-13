
def listar_libro():
    libro = ""
    with open("datos/libros.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            codigoL, titulo, autor, año, categoria, cod_socio  = line.strip().split(",", 5)
            libro += f"{codigoL} | {titulo} | {autor} | {año} | {categoria} | {cod_socio}\n"
        return libro
    
def listar_libro_disponible():
    libro = ""
    with open("datos/libros.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            codigoL, titulo, autor, año, categoria, cod_socio  = line.strip().split(",", 5)
            if cod_socio == "none":
                libro += f"{codigoL} | {titulo} | {autor} | {año} | {categoria} | {cod_socio}\n"
            else:
                continue
    return libro