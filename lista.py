print("LISTA DE TAREAS")
tareas= input("agrega tu primera tarea")
lista_tareas=[tareas]
while True:
    agregar=input("quieres agregar algo mas?")

    if agregar.lower()=="no":
        print ("perfecto esta es su lista",lista_tareas)
        break
    elif agregar.lower()=="si":
        nueva_tarea=input("escribe la nueva tarea")
        lista_tareas.append(nueva_tarea)
        print("esta es tu lista",lista_tareas)
    else:
        print("no entiendo la respuesta.Por favor escribe si o no")
while True:
    borrar= input("quieres borrar alguna tarea?")
    if borrar=="no":
        print("perfecto, esta es tu lista",lista_tareas)
        break
    elif borrar=="si":
            borrar_tarea=input("escribe que tarea deseas borrar")
            if borrar_tarea in lista_tareas:
                lista_tareas.remove(borrar_tarea)
                print("Perfecto, esta es tu lista", lista_tareas)
            else: 
                print("eso no esta en la lista de tareas")
            
    else:
        print("no entiendo la respuesta.Por favor escribe si o no")

            