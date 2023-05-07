import numpy as np
import csv



class MateriasAprobadas:
    __dni:str
    __nombreMateria:str
    __fecha:int
    __nota:int
    __aprobacion:chr
    def __init__(self,dni,nombreMateria,fecha,nota,aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    def __str__(self):
        return f"DNI >> {self.__dni} | Nombre de materia >> {self.__nombreMateria} | Fecha >> {self.__fecha} | Nota >> {self.__nota} | Aprobacion >> {self.__aprobacion}"

class Alumno:
    __dni:str
    __apellido:str
    __nombre: str
    __carrera: str
    __añoquecursa: int
    __materia: MateriasAprobadas
    def __init__(self,dni,apellido,nombre,carrera,añoquecursa,materia):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__añoquecursa = añoquecursa
        self.__materia = materia
    def __str__(self):
        return f"Alumno {self.__nombre} {self.__apellido} | DNI {self.__dni} | Carrera {self.__carrera} y Año que Cursa {self.__añoquecursa}"
    def calcular_promedio(self):
        calificacion = [self.__materia.__nota]
        for self.__materia.__nota in self.__materia:
            promedio = np.mean(calificacion)
            return promedio
    def calcular_promedio_sin_aplaso(self):
        calificacion = [self.__materia.__nota]
        for self.__materia.__nota in self.__materia:
            if self.__materia.nota >= 4:
                promedio = np.mean(calificacion)
            else:
                promedio = 0
        return promedio
    def __it__ (self,otro:int):
        if self.__añoquecursa == otro.__añoquecursa:
            resultado = self.__apellido < otro.__apellido
        else:
            resultado = self.__añoquecursa < otro.__añoquecursa
class Gestoralumnos:
    __lista_alumnos:list
    __alumno:Alumno
    def __init__(self,lista_alumno,alumno):
        self.__lista_alumnos = lista_alumno
        self.__alumno = alumno
    def cargar_alumnos(self, datos:list):
        self.__lista_alumnos = []
        for i in datos:
            self.__lista_alumnos.append(datos[i])

    def busqueda(self,dni):
        while self.__alumno:
            if self.__alumno.__dni == dni:
                return self.__alumno.calcular_promedio
    def ordenar_alumnos(self):
        i:int
        j:int
        i = 1
        valor:int
        while i in (self.__lista_alumnos):
            valor = self.__lista_alumnos[i]
            j = i-1
            while ((j > 0) and (valor < self.__lista_alumnos[j])):
                self.__lista_alumnos[j+1] = self.__lista_alumnos[j]
                j += 1
                self.__lista_alumnos[j+1] = valor
    def mostrar_listado(self):
        return self.__lista_alumnos
class GestorMaterias:
    __lista_materias: list
    __materias:MateriasAprobadas
    __gestor: Gestoralumnos
    __alumno: Alumno
    def __init__(self,lista_materias,materias,gestor,alumno):
        self.__lista_materias = lista_materias
        self.__materias = materias
        self.__gestor = gestor
        self.__alumno = alumno
    def cargar_materias(self,dato:list):
        self.__lista_materias = []
        for i in dato:
            self.__lista_materias.append(dato[i])
    def buscar_alumno(self,aux_materia):
        lista_aprobados = []
        while self.__materias:
            if self.__materias.__nombreMateria == aux_materia and self.__materias.__nota >= 7 and self.__materias.__aprobacion == 'P':
                aprobados = self.__gestor.busqueda(self.__materias.__dni)
                if aprobados:
                    lista_aprobados.append(aprobados,self.__materias.__fecha,self.__materias.__nota,self.__alumno.__añoquecursa)
#Algoritmo principal
def new_func(datos_guardados, gestor_alumnos):
    gestor_alumnos.cargar_alumnos(datos_guardados)

def new_func1(info_guardada, gestor_materias):
    gestor_materias.cargar_materias(info_guardada)

if __name__ == '__main__':
    with open('alumnos.csv', 'r') as archivo:
        lector = csv.reader(archivo,delimiter=';')
        datos = []
        for datos in lector:
            dni = str(datos[0].split(';')[0])
            apellido = str(datos[1].split(';')[0])
            nombre = str(datos[2].split(';')[0])
            carrera = str(datos[3].split(';')[0])
            datos_guardados = (datos[0], datos[1], datos[2], datos[3])
    with open('materiasAprobadas.csv','r',encoding='utf-8') as archivo:
        lector = csv.reader(archivo,delimiter=';')
        datos_materia = []
        for datos_materia in lector:
            dni = str(datos_materia[0].split(';')[0])
            nombre_materia = str(datos_materia[1].split(';')[0])
            fecha = datos_materia[2].split('/')[0]
            nota = (datos_materia[3].split(';')[0])
            aprobacion = (datos_materia[4].split(';')[0])
            info_guardada = (datos_materia[0], datos_materia[1], datos_materia[2], datos_materia[3], datos_materia[4])
    gestor_alumnos = Gestoralumnos
    new_func(datos_guardados, gestor_alumnos)
    gestor_materias = GestorMaterias
    new_func1(info_guardada, gestor_materias)

