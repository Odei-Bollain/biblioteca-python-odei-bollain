
def listar_libro():
    libro = ""
    with open("datos/libros.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            codigoL, titulo, autor, año, categoria  = line.strip().split(",", 4)
            libro += f"{codigoL} | {titulo} | {autor} | {año} | {categoria}\n"
        return libro