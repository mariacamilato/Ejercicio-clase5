class Mascota:
    def __init__ (self):
        self.__nombre=""
        self.__historia=0 
        self.__tipo=""
        self.__peso=""
        self.__fechaIngreso=""
        self.__listaMedicamentos={}

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

class Medicamento: 
    def __init__(self):
        self.__nombre=""
        self.__dosis=""
    
    def getNombre(self):
        return self.__nombre
    
    def getDosis(self):
        return self.__dosis 
    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setDosis(self,dosis):
        self.__dosis=dosis 

class Sistema:
    def __init__(self):
        self.__listadoMascotas=[]
    
    def ingresarMascotas(self,mascota):
        self.__listadoMascotas.append(mascota)
    
    def verFechaIngreso(self,masc,historia):
        for i in self.__listadoMascotas:
            if historia == masc.getHistoria():
                return masc.getFechaIngreso()
        return None

    def verNumeroMascotas(self):
        return len(self.__listadoMascotas)
    
    def verMedicamento(self,masc,historia):
        for i in self.__listadoMascotas:
            if historia == masc.getHistoria():
                return masc.getListaMedicamentos()
        return None 
    
    def eliminarMascota(self,masc,historia):
        for i in self.__listadoMascotas:
            if historia == masc.getHistoria():
                self.__listadoMascotas.remove(masc)
                return True 
        return False 
    
    def verificarExiste(self,masc,historia):
        for i in self.__listadoMascotas:
            if historia == masc.getHistoria():
                return True 
        return False 
    
    def salir(self):
        return ("¡¡¡ Usted ha salido exitosamente de esta sección !!!")

def verifica(a):
    while True:
        try:
            int(a)
            return(a)
            break
        except ValueError:
            a=input("POR FAVOR INGRESE VALORES NÚMERICOS >>> ")

def main():
    servicio=Sistema() 
    masc=Mascota()
    while True:
        menu=input('''\nSeleccione: 
                   1. Agregar mascota
                   2. Ver Fecha de ingreso
                   3. Ver número de mascotas en el servicio
                   4. Ver medicamentos administrados a la mascota
                   5. Eliminar Mascota
                   6. Salir\n >>>''')
        if menu =="1":
            if servicio.verNumeroMascotas() >= 10:
                print("¡¡¡ No hay espacio para registro de mascotas !!!")
                continue
            historia=(input("Ingrese el número de historia de la mascota >>> "))
            historia=verifica(historia)
            if servicio.verificarExiste(masc,historia) == False:
            
                nombre=input("Ingrese el nombre de la mascota >>> ")
                tipo=input("¿Qué tipo de mascota es? >>> ")
                peso=input("Ingrese el peso de la mascota en lb >>> ")
                peso=verifica(peso)
                fecha=input("Ingrese la fecha de ingreso de la mascota >>> ")
                cantidadm=int(input("Ingrese la cantidad de medicamentos que tiene la mascota >>> "))
                listaMed=[]

                for i in range (0,cantidadm):
                    nombre_med=input(f"Ingrese el nombre del medicamento {i+1} >>> ")
                    dosis=input(f"Ingrese la dosis del medicamento {i+1} en mm>>> ")
                    dosis=verifica(dosis)
                    medica=Medicamento()
                    medica.setNombre(nombre_med)
                    medica.setDosis(dosis)
                    listaMed.append(medica)
                masc=Mascota()
                masc.setNombre(nombre)
                masc.setHistoria(historia)
                masc.setPeso(peso)
                masc.setTipo(tipo)
                masc.setFechaIngreso(fecha)
                masc.setListaMedicamentos(listaMed)
                servicio.ingresarMascotas(masc)
            else:
                print(" ¡¡¡Ya existe una mascota con ese número de historia !!! ")
        
        elif menu =="2":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            fecha= servicio.verFechaIngreso(masc,historia) 
            if fecha!=None:
                print(f"La fecha de ingreso de la mascota fue >>> {fecha}")
            else:
                print("¡¡¡ La historia clínica no pertene a ninguna mascota !!! ")
        
        elif menu =="3":
            numero=servicio.verNumeroMascotas()
            print(f"El número de mascotas ingresados hasta el momento es {numero}")
        
        elif menu =="4":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            medicamento= servicio.verMedicamento(masc,historia)
            if medicamento!=None:
                print("Los medicamentos de esta mascota son: >>> ")
                for m in medicamento:
                    print(f" Nombre de medicamento ---> {m.getNombre()}")
                    print(f" Dosis de medicamento ---> {m.getDosis()}")
            else:
                print("¡¡¡ No hay ninguna mascota que coincida con el número de historia !!! ")
        
        elif menu =="5":
            historia=input("Ingrese el número de historia de la mascota >>> ")
            historia=verifica(historia)
            eliminar=servicio.eliminarMascota(masc,historia)
            if eliminar == True:
                print("¡¡¡Mascota eliminada con éxito!!!")
            else:
                print(" ¡¡¡ No hay ninguna mascota que coincida con el número de historia !!! ")
        
        elif menu =="6":
                salir=input(" SI DESEA SALIR MARQUE 1, DE LO CONTRARIO MARQUE 2 >>> ")
                if salir=="1":
                    print(servicio.salir())
                    exit()
                elif salir=="2":
                    continue
        else:
            print("<<< OPCIÓN INCORRECTA, INTENTELO DE NUEVO >>>")

if __name__=="__main__":
    main()                

                    
















            











            