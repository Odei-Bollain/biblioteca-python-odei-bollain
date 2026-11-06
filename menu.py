class Menu:
    cerrar = 0
    while (cerrar == 0):
        print("------------BIBLIOTECA------------")
        print("1.Mostrar lista libros")
        print("2.Mostrar libros disponibles")
        print("3.Buscar libro por titulo")
        print("4.Prestar libro")
        print("5.Devolver libro")
        print("6.Mostrar socio con libro")
        print("7.Añadir libro")
        print("8.Salir")
        print("----------------------------------")
        num = input("Indica un numero la opción que requieras\n")

        match num:
            case 1:
                print()
                break
            case 2:
                print
                break
            case 3:
                print
                break
            case 4:
                print
                break
            case 5:
                print
                break
            case 6:
                print
                break
            case 7:
                print
                break
            case 8:
                print("¿Seguro que quieres cerrar el programa?\n")
                cerrar = 1