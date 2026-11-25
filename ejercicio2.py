def calificaciones():

    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    cantidad_evaluaciones = int(input("Ingrese la cantidad de evaluaciones: "))

    estudiantes = []

    for i in range(cantidad_estudiantes):
        nombre = input("Ingrese el nombre del estudiante: ")
        evaluaciones = []
        for j in range(cantidad_evaluaciones):
            nombre_evaluacion = input("Ingrese el nombre de la evaluación: ")
            nota = int(input("Ingrese la nota : "))

            if nota >= 0 and nota <= 5:

                evaluaciones.append({
                    "nombre_evaluacion": nombre_evaluacion,
                    "nota": nota
                })

            else:
                print("Las notas solo pueden estar entre 0 y 5")
                exit()


        estudiantes.append({
            "nombre":nombre,
            "evaluaciones": evaluaciones
        })

    #Mostrar calificaciones
    print(estudiantes)


    #Consultar estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante que desea consultar: ")

    #Buscar estudante por nombre
    promedio = 0
    for i in range(len(estudiantes)):

        if(nombre_estudiante == estudiantes[i]["nombre"]):
            print(f"Notas del estudiante: {estudiantes[i]["evaluaciones"]}")
            suma = 0
            for j in range(len(estudiantes[i]["evaluaciones"])):
                suma = suma + estudiantes[i]["evaluaciones"][j]["nota"]

            
            promedio = suma / len(estudiantes[i]["evaluaciones"])

    print(promedio)



calificaciones()