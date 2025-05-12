
#aca iniciamos nuestro diccionario vacio
biblioteca={}

#funcion para agregar libros
def addBook():
    print("--"*5)
    print("**Crear libro**")
    print("--"*5)

    id=input("Ingresa el ID del Libro--->")

    while id .isalpha():
        print("Invalid id solo numeros")
        id=input("Ingresa el ID valido del Libro--->")

    
    titulo=input("Ingresa el titulo del Libro--->")
   
    autor=input("Ingrese el autor del Libro-->")
    
    publicacionYear=input("Ingrese el año de publicacion del Libro-->")

    biblioteca[id]={
        "titulo":titulo,
        "autor":autor,
        "año":publicacionYear
        }

    print("----"*20)
    print("Libro Agreagado con Exito ► ► ► ► ► ► ►")
    print(biblioteca)
    print("-----"*20)

#funcion para buscar libro
def searchBook():
    print("--"*10)
    print("*Buscar libro**")
    print("--"*10)

    #validamos que libros disponibles hay  o si la bilioteca se encuentra vacia antes de imprimir

    validarBiblioteca=bool(biblioteca)

    if validarBiblioteca==False:
        print("Biblioteca Vacia Agrega libros")
        print("--"*20)
    else:
        print("--"*20)
        print("Libros disponibles \n",biblioteca)
        print("--"*20)
        print("Menu \n 1)Buscar Por ID \n 2)Buscar Por TITULO")

        opcion=input("Ingresa la opcion-->")

        while opcion .isalpha():
            print("Opcion Invalida")
            opcion=input("Ingresa una  opcion valida-->")


        if opcion=="1":
            print("----"*10)
            print("Opcion de Busqueda por ID")
            print("*****")

            idConsulta=input("Ingrese El ID A BUSCAR--->")

            while idConsulta .isalpha():
                print("ID INVALIDO ")
                idConsulta=input("Ingrese un ID valido A BUSCAR--->")
            
            if idConsulta in biblioteca:
                print("----"*15)
                print("DESCRIPCION")
                libroEncontrado=biblioteca[idConsulta]
                print(f"Titulo: {libroEncontrado["titulo"]} \n Autor: {libroEncontrado["autor"]} \n Año: {libroEncontrado["año"]}")
                
            else:
                print("No existe ese libro con ese ID")

        if opcion == "2":
            print("----"*10)
            print("Opcion de Busqueda por TITULO")
            print("*****")

            tituloConsulta=input("Ingrese El TITULO A BUSCAR--->")

            while tituloConsulta .isnumeric():
                print("TITULO INVALIDO ")
                tituloConsulta=input("Ingrese un TITULO valido A BUSCAR--->")

            for idConsulta , titulo in biblioteca.items():
                if tituloConsulta in titulo["titulo"]:

                    print("DESCRIPCION")

                    print(f"ID: {idConsulta} \n TITULO: {titulo["titulo"]} \n AUTOR: {titulo["autor"]} \n  AÑO: {titulo["año"]} ")
                else:
                    print("Titulo No Encontrado")
                



#funcion para actualizar libro
def updateBook():
    print("--"*10)
    print("*Actualizar libro**")
    print("--"*10)
    print(biblioteca)
    print("--"*10)

    opcion=input("Digite el ID del libro que Desea Modificar-->")

    while opcion .isalpha():
        print("ID Invalido")
        opcion=input("Digite un ID valido-->")

    if opcion in biblioteca:
      
        print("-----"*12)
        print("***ESTE ID corresponde a este Libro ***")
        libroEncontrado=biblioteca[opcion]
        print(libroEncontrado)
        print("-----"*12)
        print("Que Desea Actualizar \n 1) TITULO \n 2) Autor \n 3) Año ")

        opcionActualizacion=input("Ingrese la opcion-->")

        while opcionActualizacion .isalpha():
            print("Opcion Invalidad")
            opcionActualizacion=input("Ingrese una Opcion Valida-->")
        
        if opcionActualizacion=="1":
            print("**ACTUALIZAR TITULO**")
            print(libroEncontrado)
            nuevoTitulo=input("Ingrese el nuevo Titulo del libro-->")
            libroEncontrado["titulo"]=nuevoTitulo
            print("Titulo Actualizado Satisfactoriamente ✓✓✓✓✓✓")
            print(libroEncontrado)

        elif opcionActualizacion=="2":
            print("**ACTUALIZAR AUTOR**")
            print(libroEncontrado)
            nuevoAutor=input("Ingrese el nuevo Autor del libro-->")
            libroEncontrado["autor"]=nuevoAutor
            print("Autor Actualizado Satisfactoriamente ✓✓✓✓✓✓")
            print(libroEncontrado)
        
        elif opcionActualizacion=="3":
            print("**ACTUALIZAR AÑO**")
            print(libroEncontrado)
            nuevoYear=input("Ingrese el nuevo Año del libro-->")
            libroEncontrado["año"]=nuevoYear
            print("Año Actualizado Satisfactoriamente ✓✓✓✓✓✓")
            print(libroEncontrado)

        
  #funcion para eliminar libro      
def deleteBook():
    print("--"*10)
    print("*Eliminar libro**")
    print("--"*10)
    print(biblioteca)
    print("--"*10)

    deleteBook=input("Ingresa el Id del libro que desea eliminar--->")

    while deleteBook .isalpha():
        print("ID Invalido")
        deleteBook=input("Ingresa un Id Valido--->")
    
    if deleteBook in biblioteca:
        biblioteca.pop(deleteBook)
        print("Libro Eliminado satisfactoriamente")
        print(biblioteca)
    else:
        print("No existe libro con ese ID")


#funcion para visualizar libros
def viewBooks():
        print(biblioteca)



#aca tenemos nuestro menu principal el cual es buncle infinito el cual termina cuando se de la opcion 6 salir
#donde estara el break

while True:
    print("******Binvenidos****** \n ****Biblioteca Confama**** ")
    print("---"*10)

    print("**MENU** \n 1)Crear Libro \n 2)Buscar Libro \n 3)Actualizar Libro \n 4)Eliminar Libro \n 5)Ver Libros \n 6)Salir")

    # aca preguntamos al usuario que desea hacer en nuestro sistema de acuerdo a la opcion elejida

    opcion=input("Ingresa una opcion---->")

    #realizamos la verificacion de que opcion marca el usuario 
    #hay 6 opciones , si el usuario marca una opcion no existente , le dira que es una opcion invalida
    #si ingresa una opcion valida segurira el programa
    
    if opcion=="1":
        addBook()
    elif opcion=="2":
        searchBook()
    elif opcion=="3":
       updateBook()

    elif opcion=="4":
        deleteBook()
    elif opcion=="5":
        viewBooks()
    elif opcion=="6":
       break
    else:
        print("invalid")
    
  
    
  
    
  
    
  




    


  