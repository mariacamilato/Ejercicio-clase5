class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula=int
        self.__genero=""
        self.__servicio=""

    def getNombre(self):
        return self.__nombre
    
    def getCedula(self):
        return self.__cedula
    
    def getGenero(self):
        return self.__genero
    
    def getServicio(self):
        return self.__servicio
    
    def setNombre(self,nombre):
        self.__nombre=nombre 
    
    def setCedula(self, cedula):
        self.__cedula=cedula
    
    def setGenero(self, genero):
        self.__genero=genero
    
    def setServicio(self,servicio):
        self.__servicio=servicio 
    
class Sistema:
    def __init__(self):
        self.__listadoPacientes=[]
        self.__numeroPacientes=len(self.__listadoPacientes)
        
    def ingresarPacientes(self):
        nombre=input("Ingrese el nombre del paciente >>> ")
        cedula=input("Ingrese la cédula del paciente >>> ")
        genero=input("Ingrese el género del paciente >>> ")
        servicio=input("Ingrese el servicio al cual ingresó el paciente >>> ")
        a=Paciente()
        a.setNombre(nombre)
        a.setCedula(cedula)
        a.setGenero(genero)
        a.setServicio(servicio)
        self.__listadoPacientes.append(a)
        self.__numeroPacientes=len(self.__listadoPacientes)  
       
        
    def verDatosPacientes(self):
            ide=input( "Ingrese la cédula del paciente buscar >>> ")
            for paciente in self.__listadoPacientes: 
                if ide == paciente.getCedula(): 
                    print(f"El nombre del paciente es >>> {paciente.getNombre()}")
                    print(f"La cédula del paciente es >>> {paciente.getCedula()}")
                    print(f"El género del paciente es >>> {paciente.getGenero()}")
                    print(f"El servicio al cual ingresó el paciente >>> {paciente.getServicio()}")
                    break
            else:
                print("¡¡¡DOCUMENTO NO ENCONTRADO EN LA BASE DE DATOS, intente de nuevooo!!!") 
                

    def verNumeroPacientes(self):
        print (f"Hasta el momento hay {self.__numeroPacientes} pacientes registrados") 
    
    def salir(self):
        print (">>> Usted ha salido exitosamente del sistema <<<")
    
mi_sistema=Sistema()

while True:
    menu=input("Marque:\n1.Agregar paciente \n2.Ver datos de paciente \n3.Ver número de pacientes \n4.Salir ")
    if menu=="1":
        mi_sistema.ingresarPacientes()
    elif menu=="2":
        mi_sistema.verDatosPacientes()
    elif menu=="3":
        mi_sistema.verNumeroPacientes()
    elif menu=="4":
        mi_sistema.salir()
        break
    else:
        print("INGRESÓ UNA OPCIÓN INCORRETA, INTENTE NUEVAMENTE")

