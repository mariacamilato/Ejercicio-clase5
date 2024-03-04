from datetime import datetime 
#Hacemos llamado a la libreria de datetime para el concepto de la fecha.
class Mascota:
#Este es el constructor de la clase mascota, que tiene la funcion de dar inicio a las variables o atributos.
    def __init__ (self):
        self.__nombre=""
        self.__historia=0 
        self.__tipo=""
        self.__peso=""
        self.__fechaIngreso=""
        self.__listaMedicamentos=[]
#Los atributos de esta clase tienen un nivel de encapsulamiento privado.
    def getNombre(self):
        return self.__nombre
    
    def getHistoria(self):
        return self.__historia
    
    def getTipo(self):
        return self.__tipo
    
    def getPeso(self):
        return self.__peso
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def getListaMedicamentos(self):
        return self.__listaMedicamentos 
#En esta sección se ubicaron los get, que retornaran los valores de los atributos de la clase Mascota.
    
    def setNombre(self,nombre):
        self.__nombre=nombre 

    def setHistoria(self,historia):
        self.__historia=historia
    
    def setTipo(self,tipo):
        self.__tipo=tipo
    
    def setPeso(self,peso):
        self.__peso=peso
    
    def setFechaIngreso(self,FechaIngreso):
        self.__fechaIngreso=FechaIngreso 

    def setListaMedicamentos(self,lista):
        self.__listaMedicamentos=lista
# por otra parte los set, de la clase Mascota nos permiten asignar los valores de los atributos y manejarlos fuera de la clase. 
    def verificaMedicamento(self,medi):
        for i in self.__listaMedicamentos:
            if medi == i.getNombre():
                return True
        return False 
    
    def eliminarMedicamento(self,historia):
        for i in self.__listaMedicamentos:
            if historia == i.getNombre():
                self.__listaMedicamentos.remove(i)
                return True
        return False 
#Los metodos de la clase dados por las anteriores dos funciones.
class Medicamento:
#Esta seccion es de la clase Medicamento, y el constructor.
    def __init__(self):
        self.__nombre=""
        self.__dosis=""
#atributos con nivel de encapsulamiento privado.   
    def getNombre(self):
        return self.__nombre
    
    def getDosis(self):
        return self.__dosis 
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setDosis(self,dosis):
        self.__dosis=dosis 
#los get y set de la clase medicamento que nos permiten hacer uso de los atributos fuera de ella.
class Sistema:
#La clase sistema con sus elementos contenedores que serviran para ingresar nuestros objetos mascota.
    def __init__(self):
        self.__caninos=[]
        self.__felinos=[]
        self.__listadoMascotas={"caninos":self.__caninos, "felinos": self.__felinos}
#constructor init con sus atributos y nivel de encapsulamiento privado.  
    def ingresarCaninos(self,masc):
        self.__caninos.append(masc)
    
    def ingresarFelinos(self,masc):
        self.__felinos.append(masc)

    def verFechaIngreso(self,historia):
        for key in self.__listadoMascotas:
            for valor in self.__listadoMascotas[key]:
                    if historia == valor.getHistoria():
                        return valor.getFechaIngreso()
        return None 

    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos)
    
    def verMedicamento(self,historia):
        for key in self.__listadoMascotas:
            for valor in self.__listadoMascotas[key]:
                if historia == valor.getHistoria():
                    return valor.getListaMedicamentos()
        return None 
    
    def eliminarMascota(self,historia):
        for key in self.__listadoMascotas:
            for valor in self.__listadoMascotas[key]:
                if historia == valor.getHistoria():
                    self.__listadoMascotas[key].remove(valor)
                    return True 
        return False 
    
    def verificarExiste(self,historia):
        for key in self.__listadoMascotas:
            for valor in self.__listadoMascotas[key]:
                    if historia == valor.getHistoria():
                        return True 
        return False 
    
    def salir(self):
        return ("¡¡¡ Usted ha salido exitosamente de esta sección !!!")
    
    def fecha(self):
        while True:
            fecha=input("Ingrese la fecha en formato DD/MM/AA >>>")
            try:
                fe=datetime.strptime(fecha, "%d/%m/%y")
                return fe
                break 
            except ValueError:
                print("¡¡¡Formato incorrecto, intente nuevamente!!!")
#Hasta esta parte se evidencian los métodos de nuestra clase sistema, que seran de utilidad en el menú del programa.
def verifica(a):
    while True:
        try:
            int(a)
            return(a)
            break
        except ValueError:
            a=input("POR FAVOR INGRESE VALORES NÚMERICOS >>> ")
#Esta funcion esta por fuera de todas las clases, se implementó para hacer verificación de 
#valores númericos (solo no verifiqué el # de medicamentos a ingresar :( ...)
def main():
#Con Main, la funcion principal, hacemos la ejecución de nuestro programa.
    servicio=Sistema() 
    masc=Mascota() #Asignamos objetos, para incluir en el menú.
    while True:
        menu=input('''\nSeleccione: 
                   1. Agregar mascota
                   2. Ver Fecha de ingreso
                   3. Ver número de mascotas en el servicio
                   4. Ver medicamentos administrados a la mascota
                   5. Eliminar Mascota
                   6. Eliminar Medicamento de una mascota
                   7. Salir\n >>>''')
        if menu =="1":
            if servicio.verNumeroMascotas() >= 10:
                print("¡¡¡ No hay espacio para registro de mascotas !!!")
                continue
            historia=(input("Ingrese el número de historia de la mascota >>> "))
            historia=verifica(historia)
            if servicio.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota >>> ")
                tipo=input("""¿Qué tipo de mascota es? Marque
                           1.PARA CANINOS
                           2.PARA FELINOS >>> """)
                peso=input("Ingrese el peso de la mascota en lb >>> ")
                peso=verifica(peso)
                fecha=servicio.fecha()
                cantidadm=int(input("Ingrese la cantidad de medicamentos que tiene la mascota >>> "))
                listaMed=[]

                for i in range (0,cantidadm):
                    while True:
                        nombre_med=input(f"Ingrese el nombre del medicamento {i+1} >>> ")
                        medicamento_existente = False 
                        for n in listaMed:
                            if nombre_med == n.getNombre():
                                #En esta parte se hace evidente el POLIMORFISMO
                                #pues hay dos metodos con el mismo nombre
                                #en clase Medicamento y en clase Mascota
                                print("Este medicamento ya se encuentra en la lista")
                                medicamento_existente = True  
                                break
                        if not medicamento_existente:
                            dosis=input(f"Ingrese la dosis del medicamento {i+1} en mm >>> ")
                            dosis=verifica(dosis)
                            medica=Medicamento()
                            medica.setNombre(nombre_med)#POLIMORFISMO
                            medica.setDosis(dosis)
                            listaMed.append(medica)
                            break 
                masc=Mascota()
                masc.setNombre(nombre)#POLIMORFISMO
                masc.setHistoria(historia)
                masc.setPeso(peso)
                masc.setTipo(tipo)
                masc.setFechaIngreso(fecha)
                masc.setListaMedicamentos(listaMed)
                if tipo=="1":
                    servicio.ingresarCaninos(masc)
                else:
                    servicio.ingresarFelinos(masc)
            else:
                print(" ¡¡¡Ya existe una mascota con ese número de historia !!! ")
        
        elif menu =="2":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            fecha= servicio.verFechaIngreso(historia) 
            if fecha!=None:
                print(f"La fecha de ingreso de la mascota fue >>> {fecha}")
            else:
                print("¡¡¡ La historia clínica no pertene a ninguna mascota !!! ")
        
        elif menu =="3":
            numero=servicio.verNumeroMascotas()
            print(f"El número de mascotas ingresados hasta el momento es >>> {numero}")
        
        elif menu =="4":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            medicamento= servicio.verMedicamento(historia)
            if medicamento!=None:
                print("Los medicamentos de esta mascota son: >>> ")
                for m in medicamento:
                    print(f"Nombre de medicamento ---> {m.getNombre()}")
                    print(f"Dosis de medicamento ---> {m.getDosis()}")
            else:
                print("¡¡¡ No hay ninguna mascota que coincida con el número de historia ingresado !!! ")
        
        elif menu =="5":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            eliminar=servicio.eliminarMascota(historia)
            if eliminar == True:
                print("¡¡¡Mascota eliminada con éxito!!!")
            else:
                print(" ¡¡¡ No hay ninguna mascota que coincida con el número de historia ingresado !!! ")
        
        elif menu=="6":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            medicamento= servicio.verMedicamento(historia)
            if medicamento!=None:
                print("Los medicamentos de esta mascota son: >>> ")
                for m in medicamento:
                    print(f"Nombre de medicamento ---> {m.getNombre()}")
                    print(f"Dosis de medicamento ---> {m.getDosis()}")
                    x=input("Ingrese el nombre del medicamento que desea eliminar >>>")
                    eliminado=masc.eliminarMedicamento(x)
                    if eliminado== True:
                        print("<<< Medicamento eliminado con éxito >>>")
            else:
                print(" ¡¡¡ No hay ninguna mascota que coincida con el número de historia ingresado !!! ")

        
        elif menu =="7":
                salir=input(" SI DESEA SALIR MARQUE 1, DE LO CONTRARIO MARQUE 2 >>> ")
                if salir=="1":
                    print(servicio.salir())
                    exit()
                elif salir=="2":
                    continue
        else:
            print("<<< OPCIÓN INCORRECTA, INTENTELO DE NUEVO >>>")
#Los anteriores fragmentos contienen el menú de nuestro código, en esta ocasión no se presenta herencia.
if __name__=="__main__":
    main()                

                    
















            











            