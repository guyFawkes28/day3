agenda={}

def addContacto():
    global agenda
    print("----"*15)
    print("****Añadir Contacto****")
    name=input("Nombre--->")

    if name ==agenda.get("nombre"):
        print("Ya existe contacto con ese nombre")
    
    else:
        phone=input("Telefono--->")
        email=input("Email--->")

        agenda={
        "nombre":name,
        "phone":phone,
        "email":email
        }
        print("----"*10)
        print(agenda)
        print("----"*10)
        print("Contacto creado Satisfactoriamente °°°°°°°°")
    
def showContacto():
   
    print("------"*10)
    print("Tus Contactos")

    estadoAgenda=bool(agenda)

    if estadoAgenda==False:
        print("NO HAY CONTACTOS")
    
    else:
        print(agenda)
        print("---"*20)
        contactoBuscar=input("Ingresa El Nombre Del contacto--->")

  
        if contactoBuscar==agenda.get("nombre"):
            print("----"*15)
            print("***Datos Basicos***")
            print("Nombre: ",agenda.get("nombre"))
            print("Telefono:",agenda.get("phone"))
            print("Email:",agenda.get("email"))
        else:
            print("Este nombre de contacto no existe")
        
def updateContacto():
    print("-----"*15)
    print("**ACTUALIZAR CONTACTO**")
    print(agenda)

    nombreEditar=input("Ingresa nombre del contacto a editar-->")

    if nombreEditar==agenda.get("nombre"):
        print("----"*15)
        print("Que Desea Editar \n 1)Numero de Telefono \n 2)Email")
        opcion=input("Escoje Una Opcion---->")
        
        if opcion=="1":
            print("**Datos Basicos**")
            print("Nombre: ",agenda.get("nombre"))
            print("Telefono:",agenda.get("phone"))
            print("Email:",agenda.get("email"))

            nuevoTelefono=input("Digite el nuevo telefono---->")
            agenda["phone"]=nuevoTelefono
            print("-----"*15)
            print("ACTUALIZADO SATISFATORIAMENTE")
            print("---"*15)
            print(agenda)
            print("----"*15)
        
        if opcion=="2":
            print("**Datos Basicos**")
            print("Nombre: ",agenda.get("nombre"))
            print("Telefono:",agenda.get("phone"))
            print("Email:",agenda.get("email"))

            nuevoEmail=input("Digite el nuevo email---->")
            agenda["email"]=nuevoEmail
            print("-----"*15)
            print("ACTUALIZADO SATISFATORIAMENTE")
            print("---"*15)
            print(agenda)
            print("----"*15)


    else:
        print("Opcion invalida")


def deleteContacto():
    global agenda
    print("-----"*15)
    print("**ELIMINAR CONTACTOS**")
    
    estadoAgenda=bool(agenda)

    if estadoAgenda==False:
        print("NO HAY CONTACTOS")
    
    else:

        print(agenda)
        opcion=input("Digite 1 para eliminar contactos--->")

        if opcion=="1":
            agenda.clear()
            print("Contacos eliminados satisfactoriamente °°°°°°°")
        else:
            print("opcion invalida")

while True:
    print("********************")
    print("AGENDA DE CONTACTOS")
    print("***MENU***")
    print(" 1)Crear Contacto \n 2)Ver Contactos \n 3)Actualizar Contacto \n 4)Eliminar Contacto \n 5)Salir")

    opcion=input("Ingrese Una Opcion-->")

    if opcion=="1":
        addContacto()
    elif opcion=="2":
        showContacto()
    elif opcion=="3":
        updateContacto()
    elif opcion=="4":
        deleteContacto()
    elif opcion=="5":
        break
   
    else:
        print("Invalid opcion")
    
        