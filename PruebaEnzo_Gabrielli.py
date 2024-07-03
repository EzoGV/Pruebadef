import csv
import os

biblioteca = []
archivolibros = "biblioteca.csv"

def leerdatos():
    if os.path.exists(archivolibros):
        with open(archivolibros, "r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                biblioteca.append(fila)

def almacenardatos():
    with open(archivolibros, "w", newline="") as archivo:
        listas = ["Titulo", "Autor", "Genero"]
        escritor = csv.DictWriter(archivo, fieldnames=listas)
        escritor.writeheader()
        for libro in biblioteca:
            escritor.writerow(libro)

def registrarlibro():
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    genero = input("Ingrese el género: ")
    libro = {"Titulo": titulo, "Autor": autor, "Genero": genero}
    biblioteca.append(libro)
    almacenardatos()
    print("Libro registrado con éxito!")

def consultarporautor():
    autor = input("¿Qué autor desea buscar? ")
    encontrados = [libro for libro in biblioteca if libro["Autor"].lower() == autor.lower()]
    if encontrados:
        print("Libros encontrados:")
        for libro in encontrados:
            print(f"Título: {libro['Titulo']}, Género: {libro['Genero']}")
    else:
        print("No se encontró el autor.")

def listadelibros():
    if biblioteca:
        print("Lista de libros registrados:")
        for libro in biblioteca:
            print(f"Título: {libro['Titulo']}, Autor: {libro['Autor']}, Género: {libro['Genero']}")
    else:
        print("No se encuentra registrado ningún libro en su biblioteca.")

def menuprincipal():
    leerdatos()
    while True:
        print("..Bienvenido a tu biblioteca virtual..")
        print("1. Registro de libros")
        print("2. Búsqueda de libros por autor")
        print("3. Mostrar libros en la biblioteca")
        print("4. Salir")
        op = input("Seleccione una opción: ")
        if op == '1':
            registrarlibro()
        elif op == '2':
            consultarporautor()
        elif op == '3':
            listadelibros()
        elif op == '4':
            print("Saliendo del programa..")
            break
        else:
            print("No se encontró opción, seleccione una válida..")

if __name__ == "__main__":
    menuprincipal()      
