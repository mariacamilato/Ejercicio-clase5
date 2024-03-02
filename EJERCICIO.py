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
        
    def ingresarPacientes(self,paciente):
        self.__listadoPacientes.append(paciente)
        return True
    
    def verificarPacientes(self,cedula):
        for p in self.__listadoPacientes:
            if cedula==p.getCedula():
                return True
        return False 
    
    def verDatosPacientes(self,cedula):
            if self.verificarPacientes(cedula)==False:
                return None 
            for p in self.__listadoPacientes:
                if cedula == p.getCedula():
                    return p           

    def verNumeroPacientes(self):
        return (f"Hasta el momento hay {len(self.__listadoPacientes)} pacientes registrados") 
    
    def salir(self):
        return (">>> Usted ha salido exitosamente del sistema <<<")
    
def main(): 
    mi_sistema=Sistema()
    while True:
        menu=input("Marque:\n1.Agregar paciente \n2.Ver datos de paciente \n3.Ver número de pacientes \n4.Salir ")
        if menu=="1":
            cedula=input("Ingrese la cédula del paciente >>> ")
            if mi_sistema.verificarPacientes(cedula)== False:
                nombre=input("Ingrese el nombre del paciente >>> ")
                genero=input("Ingrese el género del paciente >>>")
                servicio=input("Ingrese el servicio al cual ingresó el paciente >>>")
                p=Paciente()
                p.setCedula(cedula)
                p.setNombre(nombre)
                p.setGenero(genero)
                p.setServicio(servicio)
                mi_sistema.ingresarPacientes(p)
            else:
                 print("¡¡¡YA EXISTE UN PACIENTE CON ESE NÚMERO DE DOCUMENTO!!!")

        elif menu=="2":
           cedula=input("Ingrese la cédula del paciente >>> ")
           p= mi_sistema.verDatosPacientes(cedula)
           if p != None:
               print(f"La cédula del paciente es >>> {p.getCedula()}")
               print(f"El nombre del paciente es >>>{p.getNombre()}")
               print(f"El género del paciente es >>> {p.getGenero()}")
               print(f"El servicio al cual ingresó el paciente es >>> {p.getServicio()}")
           else:
               print("¡¡¡NO EXISTE UN PACIENTE CON ESE NÚMERO DE DOCUMENTO!!!")

        elif menu=="3":
            print(mi_sistema.verNumeroPacientes())

        elif menu=="4":
            print(mi_sistema.salir())
            break
        else:
            print("INGRESÓ UNA OPCIÓN INCORRETA, INTENTE NUEVAMENTE")

if __name__ == "__main__": 
    main()

