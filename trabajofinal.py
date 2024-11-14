estudiantes = []
def agregar_estudiante (nombre, id, edad, genero, telefono):
  estudiante = {
      "nombre": nombre,
      "id": id,
      "edad": edad,
      "genero": genero,
      "telefono": telefono
      }
  estudiantes.append(estudiante)
  print(f"Estudiante{nombre} agregado exitosamente.\n")
def visualizar_estudiantes ():
  if not estudiantes:
    print("No hay estudiantes registrados.\n")
  else:
    for idx, estudiante in enumerate(estudiantes, start=1):
      print(f"{idx}. Nombre:{estudiante ['nombre']}, Id: {estudiante['id']}, Edad: {estudiante['edad']}, Genero: {estudiante['genero']}, Telefono: {estudiante['telefono']}")
def actualizar_estudiante (id, nueva_edad=None, nuevo_telefono=None):
  for estudiante in estudiantes:
    if estudiante["id"] == id:
      if nueva_edad:
       estudiante["edad"]= nueva_edad
      if nuevo_telefono:
        estudiante["telefono"]= nuevo_telefono
    print(f"Estudiante con teledono {telefono} actualizado.\n")
    print ("Estudiante no encontrado.\n")
def menu ():
  while True:
    print("Sistema de Gestión de Estudiantes")
    print("1. Agregar Estudiante")
    print("2. Mostrar estudiante")
    print("3. Actualizar estudiante")
    print("4. Salir")
    opcion= input("Seleccione una opción: ")
    if opcion== "1":
      nombre = input("Ingrese el nombre del estudiante: ")
      id = input("Ingrese el id del estudiante: ")
      edad = input("Ingrese la edad del estudiante: ")
      genero = input("Ingrese el genero del estudiante: ")
      telefono = input("Ingrese el teléfono del estudiante: ")
      agregar_estudiante(nombre, id, edad, genero, telefono)
    elif opcion=="2":
      visualizar_estudiantes()
    elif opcion=="3":
      id = input("Ingrese el id del estudiante a actualizar: ")
      nueva_edad =input("Ingrese la edad nueva: ")
      nuevo_telefono =input("Ingrese el numero de teléfono actualizado: ")
      nueva_edad = nueva_edad if nueva_edad else None
      nuevo_telefono = nuevo_telefono if nuevo_telefono else None
      actualizar_estudiante(id, nueva_edad, nuevo_telefono)
    elif opcion =="4":
      print("Saliendo del sistema.")
      break
    else:
      print("Opción invalida, intente nuevamente.\n")
  menu()
