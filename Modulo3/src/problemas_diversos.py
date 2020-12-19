


# Pregunta 1

def ingreso_notas(num_alumnos):
    listado_alumnos=[]

    for i in range(num_alumnos):
        nomb=input("Ingrese el nombre completo del alumno {i}: ".format(i=i))
        nota1=int(input("Ingrese la nota 1 del alumno "))
        nota2=int(input("Ingrese la nota 2 del alumno "))
        nota3=int(input("Ingrese la nota 3 del alumno "))
        alumnos={'nombre':nomb,'notas':[nota1,nota2,nota3]}
        listado_alumnos.append(alumnos)
    
    return listado_alumnos


def cant_aprobados(listado):
    prom_apro ={
        'aprobado':[],
        'desaprobado':[]
    }

    for name in listado:
        prom = sum(name['notas']) / 3
        if prom >=4:
            prom_apro['aprobado'].append(prom)
            continue
        prom_apro['desaprobado'].append(prom)

    print('numero de alumnos aprobados: {}'.format(len(prom_apro['aprobado'])))
    print('numero de alumnos aprobados: {}'.format(len(prom_apro['desaprobado'])))

    return prom_apro


if __name__ == "__main__":
    # 1. Ingresando listado alumnos
    # listado = ingreso_notas(int(input("Ingrese el número de alumnos a ser registrados: ")))

    

    listado = [{'nombre': 'Gonzalo', 'notas': [7, 7, 8]}, {'nombre': 'Victoria', 'notas': [5, 6, 7]}]

    print(listado)
    # 2. Aprobado - Desaprobado
    notas = cant_aprobados(listado)

    # 3. 
    
    promedio_curso = (sum(notas['aprobado']) + sum(notas['desaprobado']))/ len(listado)
    print('Promedio del curso {}'.format(promedio_curso))


