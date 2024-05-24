import csv
def calculate_grade(Practica01, Practica02, Practica03, Examen, 
                    Recuperacion, Actitud):
    Examen2 = [Examen, Recuperacion]
    total_practicas = Practica01 + Practica02 + Practica03
    NotaFinal = total_practicas/3 * 0.3 + max(Examen2)* 0.6 + Actitud * 0.1
    NotaFinal = round(NotaFinal, 2)
    if NotaFinal >= 5:  
        return NotaFinal,True
    else:
        return NotaFinal,False


def gen_correo(nombre,apellido):
    correo=""
    correo+=nombre[0]
    Long_apellido = len(apellido)
    if Long_apellido>=5:
        for i in range(0,5):
            correo+=apellido[i]
    else:
        for i in range(Long_apellido):
            correo+=apellido[i]

    dominio = "@educacion.navarra.es"
    correo+=dominio
    return correo

def process_class(fichero):
    with open(fichero, "r", newline='') as file:
        csv_clase = csv.reader(file)
        next(csv_clase)  
        
        diccionario_clase = []
        
        for alumno in csv_clase:
            nombre = alumno[0]
            apellido = alumno[1]
            practica1 = float(alumno[2].strip('"').replace(',', '.'))
            practica2 = float(alumno[3].strip('"').replace(',', '.'))
            practica3 = float(alumno[4].strip('"').replace(',', '.'))
            examen = float(alumno[5].strip('"').replace(',', '.'))
            recuperacion = float(alumno[6].strip('"').replace(',', '.'))
            actitud = float(alumno[7].strip('"').replace(',', '.'))
            
            email = gen_correo(nombre, apellido)
            nota_final, aprobado = calculate_grade(practica1, practica2, 
                                                   practica3, examen, recuperacion, actitud)
            
            diccionario_clase.append({
                'Nombre': nombre,
                'Apellido': apellido,
                'Email': email,
                'Nota': f"{nota_final}",
                'Aprobado': aprobado
            })
    
    with open("grades.csv", "w", newline='') as file2:
        cabezera = ['Nombre', 'Apellido', 'Email', 'Nota', 'Aprobado']
        grass = csv.DictWriter(file2, fieldnames=cabezera)
        
        grass.writeheader()
        for datos in diccionario_clase:
            grass.writerow(datos)


process_class('class.csv')