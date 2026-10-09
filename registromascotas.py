
 
nombre_mascotas=[""]*3
edad_mascota=[0]*3

def insertar():

    for i in range(len(nombre_mascotas)):
        nombre_mascotas[i]=input(f"ingrese nombre mascota: ")
        edad_mascota[i]=int(input(f"ingresar edad mascota: "))
def mostrar():

    for i in range(len(nombre_mascotas)):
        print(f"Nombre: {nombre_mascotas[i]}")
        Edad: {edad_mascota[i]}

def eliminar():
    nombre = input("ingresar el nombre de la mascota: ")
    for i in range(len(nombre_mascotas)):
       if  nombre_mascotas[i] == nombre:
           nombre_mascotas[i] = ""
           edad_mascota[i] =""
           print("Mascota eliminada..")
           return
       print("No se encontró la mascota")



def main():
    opcion = 0
    while opcion != 4:
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Salir")
        opcion = int(input("Elija una opcion: "))
    if opcion == 1:
       insertar()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        print("saliendo...")
    else: 
        print("opcion invalida")
    if opcion !=4: input("presione para continuar...")

main()
