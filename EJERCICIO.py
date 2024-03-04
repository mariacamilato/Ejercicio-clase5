class Paciente:
#constructor init que nos permite inicializar las variables(atributos) de la clase.
    def __init__(self):
        self.__nombre=""
        self.__cedula=int
        self.__genero=""
        self.__servicio=""
#Los atributos de la clase Pasiente presentan nivel de encapsulamiento privado.
    def getNombre(self):
        return self.__nombre
    
    def getCedula(self):
        return self.__cedula
    
    def getGenero(self):
        return self.__genero
    
    def getServicio(self):
        return self.__servicio
# Los get nos permiten retornar los valores de dichos atributos privados.   
    def setNombre(self,nombre):
        self.__nombre=nombre 
    
    def setCedula(self, cedula):
        self.__cedula=cedula
    
    def setGenero(self, genero):
        self.__genero=genero
    
    def setServicio(self,servicio):
        self.__servicio=servicio 
#Por otro lado, los set nos permiten asignar valores a estos atribitos.
#Los set y los get son los métodos que nos permiten utilizar los atributos privados fuera de la clase en los que se definen. 
class Sistema:
    def __init__(self):
        self.__listadoPacientes=[]
#Constructor de la clase sistema con el contenedor de nuestros objetos pacientes, la lista.       
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
#Las anteriores funciones son los métodos de control de nuestro sistema.   
def main(): 
#La funcion main es el metodo principal, que nos permite ejecutar el código.
    mi_sistema=Sistema()
#creamos el objeto sistema, para dar funcionalidad al menú.
    while True:
        menu=input("Marque:\n1.Agregar paciente \n2.Ver datos de paciente \n3.Ver número de pacientes \n4.Salir >>> ")
        if menu=="1":
            cedula=input("Ingrese la cédula del paciente >>> ")
            if mi_sistema.verificarPacientes(cedula)== False:
                nombre=input("Ingrese el nombre del paciente >>> ")
                genero=input("Ingrese el género del paciente >>> ")
                servicio=input("Ingrese el servicio al cual ingresó el paciente >>> ")
                p=Paciente()
                p.setCedula(cedula)
                p.setNombre(nombre)
                p.setGenero(genero)
                p.setServicio(servicio)
                mi_sistema.ingresarPacientes(p)
            else:
                 print("¡¡¡YA EXISTE UN PACIENTE CON ESE NÚMERO DE DOCUMENTO!!!")

        elif menu=="2":
           while True:
               buscar=input("""Marque:
                            1. BUSCAR PACIENTE ATRAVÉS DE SU CEDULA
                            2. BUSCAR PACIENTE ATRAVÉS DE SU NOMBRE >>> """)
               if buscar=="1":
                    cedula=input("Ingrese la cédula del paciente >>> ")
                    p= mi_sistema.verDatosPacientes(cedula)
                    if p != None:
                        print(f"La cédula del paciente es >>> {p.getCedula()}")
                        print(f"El nombre del paciente es >>>{p.getNombre()}")
                        print(f"El género del paciente es >>> {p.getGenero()}")
                        print(f"El servicio al cual ingresó el paciente es >>> {p.getServicio()}")
                        break
                    else:
                        print("¡¡¡NO EXISTE UN PACIENTE CON ESE NÚMERO DE DOCUMENTO!!!")
                        continue
               elif buscar=="2":
                   nom=input("Ingrese en nombre del paciente completo o como lo recuerde >>> ")
                   if (nom in p.getNombre())== True:
                        print(f"La cédula del paciente es >>> {p.getCedula()}")
                        print(f"El nombre del paciente es >>>{p.getNombre()}")
                        print(f"El género del paciente es >>> {p.getGenero()}")
                        print(f"El servicio al cual ingresó el paciente es >>> {p.getServicio()}")
                        break
                   else:
                       print("¡¡¡NO EXISTE UN PACIENTE CON ESE NOMBRE!!!")
                       continue

        elif menu=="3":
            print(mi_sistema.verNumeroPacientes())

        elif menu=="4":
            print(mi_sistema.salir())
            break
        else:
            print("INGRESÓ UNA OPCIÓN INCORRETA, INTENTE NUEVAMENTE")
#Lo anterior es el menú de nuestro sistema.
#En esta ocasión no se encontro ni herencia, ni polimorfismo.
if __name__ == "__main__": 
    main()

