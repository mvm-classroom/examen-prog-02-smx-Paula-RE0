#Generador de noms incorrectes per Timothée Chalamet
import random #Importo  el random para que salgan los nombres aleatorios.
import math


# Posa aquí qualsevol import que necessitis com rand, math, time...


def obtenir_nom():
    # Llista de noms incorrectes
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]

    # Llista de cognoms incorrectes
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]

    llista = []

    noms_aleatoris = random.choice(noms) #Hago que se escoja aleatorio uno de la lista de nombres y se guarde en la variable nom_aleatoris.
    cognoms_aleatoris = random.choice(cognoms) #Hago lo mismo que hice con los nombres pero con los apellidos.
    nom_complet = noms_aleatoris + cognoms_aleatoris #Pongo el nombre y el apellido aleatorio juntos en la variable nom_complet.
    return nom_complet #Saco la variable lista

    # Aquí has de construir un nom amb un nomb aleatori i un cognom aleatori de les llistes
    # retornar el nom construït

def afegir_nom(llista, nom_complet): #Llamo a la variable que tiene el nombre aleatorio.
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom
    llista.append(nom_complet) #Añado a la lista el nombre aleatorio que cree.
    print(f"Hemos Añadido el nombre {nom_complet}") #Enseño en pantalla que nombre aleatorio salio.
    
def llistar_noms(llista):
    #print("PENDENT: llistar_noms")
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista
    print("Nombres") #Le pongo titulo para que se vea mejor.
    for i in llista: #Hago un bucle de for para que se enseñen todos los nombres.
        print(f"| {llista} |") #Y ahora enseño todos los nombres que hay en la lista.    

def ordenar_noms(llista):
    print("PENDENT: ordenar_noms")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms
    llista.sort() #Ordeno de A/Z la lista
    print("Nombres") #Le pongo titulo para que se vea mejor.
    for i in llista: #Hago un bucle de for para que se enseñen todos los nombres.
        print(f"| {llista} |") #Y ahora enseño todos los nombres que hay en la lista.  



def mostrar_menu():
    # Hem de mostrar el menú que ens demanen a l'enunciatç
    print("[A] Afegir nom")
    print("[L] Listar_noms")
    print("[O] Ordenar noms")
    print("[F] Finalitzar")

def demanar_opcio():
    #print("PENDENT: demanar_opcio")
    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada    
    correcto = True    
    opcio = input("Cual de la siguientes opciones quieres").lower
    while not correcto:
        if opcio == "A":
            correcto = False
        elif opcio == "L":
            correcto = False
        elif opcio == "O":
            correcto = False
        elif opcio == "F":
            correcto = False
        else:
            print("Esa opcion no esta en la lista")
    return opcio

def gestionar_opcio(opcio, llista):
    #print("PENDENT: gestionar_opcio")
    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació 
    match opcio:
        case "A":
            afegir_nom(llista, nom_complet)
        case "L":
            llistar_noms(llista)
        case "O":
            ordenar_noms(llista)
        case "F":
            print("bye")
       




# Programa principal
llista = []
mostrar_menu()
nom_complet = obtenir_nom()
opcio = demanar_opcio()

# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
