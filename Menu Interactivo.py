# MENU INTERACTIVO


ARCHIVO = "tareas.txt"                  # nombre del archivo donde las tareas se guardan

def limpiar():                                  # limpiar consola
    print("\n" * 30)

def pausa():                                        # pausa el programa hasta que el usuario le de al ENTER
    input("\nPresione Enter para continuar")

def leer_tareas():                                                      # lee las tareas del archivo y las devuelve como lista
    try:
        with open(ARCHIVO, "r") as f:
            return [t.strip() for t in f.readlines()]
    except FileNotFoundError:
        return []
    
def guardar_tareas(tareas):                             # sobreescribe el archivo con la lista de las tareas actualizada
    with open(ARCHIVO, "w") as f:
        for tarea in tareas:
            f.write(tarea + "\n")

def agregar_tarea():                                                    # ingresa una nueva tarea y la guarda
    limpiar()
    print("/// AGREGAR TAREA ////")

    while True:                                             
        try:
            tarea = input("Ingrese la tarea: ").strip()
        except:
            print("Error al leer la entrada")
            pausa()
            return
        if tarea == "":                                     # validar que la tarea no este vacia
            print("La tarea no puede estar vacia")
        else:
            break
    try:
        with open(ARCHIVO, "a") as f:
            f.write(tarea + "\n")
    except:
        print("Error al guardar la tarea")
        pausa()
        return
    
    print("La tarea se agrego correctamente")
    pausa()
        

def ver_tareas():                                          # muestra todas las tareas que se guardaron
    limpiar()
    print("/// LISTA DE TAREAS ///")

    tareas = leer_tareas()

    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    
    pausa()

def eliminar_tarea():                                           # permite eliminar una tarea 
    limpiar()
    print("/// ELIMINAR TAREA ///")

    tareas = leer_tareas()

    if not tareas:
        print("No hay tareas para eliminarlas")
        pausa()
        return
    
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")

    while True:                                                                     
        try:
            num = int(input("\nNumero de tarea que desea eliminar: "))
            if 1 <= num <= len(tareas):
                break
            else:
                print("Numero fuera del rango")
        except ValueError:
            print(" Debe de ingresar un numero valido")

    confirmacion = input(f"Eliminar '{tareas[num-1]}'? (s/n): ").lower()                    # confirmar eliminacion

    if confirmacion == "s":
        tareas.pop(num - 1)
        guardar_tareas(tareas)
        print("Tarea eliminada")
    else:
        print("Cancelado")

    pausa()

def menu():                                                                     # menu principal del programa
    while True:
        limpiar()
        print("""
------------------------------------        
        GESTOR DE TAREAS
------------------------------------
1. Agregar Tarea
2. Ver Tareas
3. Eliminar tarea
4. Salir
------------------------------------
""")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("Saliendo del menu...")
            break
        else: 
            print("Opcion invalida")
            pausa()
            
        

menu()


# IMPORTANTE SE DEBE IMPRIMIR EN VISUAL STUDIO CODE PORQUE ESTUVE REALIZANDO PRUEBAS EN LA APLICACION DE PYTHON DE LA VERSION 3.12 Y A LA HORA DE AGREGAR UNA TAREA NO FUNCIONA LO CUAL 
# SE RECOMIENDA QUE SE EJECUTE EN VISUAL MUCHAS GRACIAS.