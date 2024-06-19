Trabajador=[]
Cargo=[]
Sueldo_Bruto=[]
Desc_Salud=[]
Desc_AFP=[]
Liquido_Pagar=[]
opcionMenu="5"
def NomTrabajador():
    verificar = True
    while verificar:
        print("\nTrabajador Nombre")
        Nombre=input("Ingrese el nombre y apellido del Trabajador: ")
        print("")
        if len(Nombre) <= 2:
            print("Error")
        else:
            print("Añadido correctamente!")
            verificar = False
            return Trabajador.append(Nombre)

def CargoTrabajador():
    verificar = True
    while verificar:
        print("\nCargo")
        print("1.- CEO\n2.- Programador\n3.- Analista\n4.- Mantenimiento")
        Puesto=input(f"Eliga el cargo a ocupar por el trabajador {Trabajador[-1]}: ")
        if Puesto == "1":
            Cargo.append("CEO")
            verificar=False
        elif Puesto == "2":
            Cargo.append("Programador")
            verificar=False
        elif Puesto == "3":
            Cargo.append("Analista")
            verificar=False
        elif Puesto == "4":
            Cargo.append("Mantenimiento")
            verificar=False
        else:
            print("Ingrese una opcion valida!")

def Sueldo():
    Verificar = True
    while Verificar:
        try:
            print("Sueldo Bruto")
            plata=int(input(f"Ingrese el sueldo bruto del trabajador {Trabajador[-1]}: "))
        except ValueError:
            print("Ingrese un valor valido!")
        else:
            return Sueldo_Bruto.append(plata)
 
while opcionMenu!="4":
    print("\n1. Registrar trabajador")
    print("2. Listar los todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del Programa")

    opcionMenu =input("Ingrese una opcion: ")
    match opcionMenu:
        case "1":
            NomTrabajador()
            CargoTrabajador()
            Sueldo()
            num1=Sueldo_Bruto[-1]*0.07
            Desc_Salud.append(int(num1))
            
            num2=Sueldo_Bruto[-1]*0.12
            Desc_AFP.append(int(num2))
            
            num3=Sueldo_Bruto[-1]-(Desc_Salud[-1]+Desc_AFP[-1])
            Liquido_Pagar.append(int(num3))
        case "2":
            for i in range(len(Trabajador)):
                print((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*300}\n"))
        case "3":
            print("¿Como desea imprimir la lista?\n1) Solo Ceo\n2) Programador\n3) Analista de datos\n4) Mantenimiento\n5) Todos los puestos")
            ops=input("Ingrese una opcion: ")
            match ops:
                case "1":
                   with open ("lista_CEO.txt", "w") as archivo:
                        for i in range(len(Trabajador)):
                            if Cargo[i]=="CEO":
                                archivo.write((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*300}\n"))
                
                case "2":
                   with open ("lista_Programador.txt", "w") as archivo:
                       for i in range(len(Trabajador)):
                            if Cargo[i]=="Programador":
                                archivo.write((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*300}\n"))
                
                case "3":
                   with open ("lista_Analista.txt", "w") as archivo:
                       for i in range(len(Trabajador)):
                            if Cargo[i]=="Analista":
                                archivo.write((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*300}\n"))
                
                case "4":
                   with open ("lista_Mantenimiento.txt", "w") as archivo:
                       for i in range(len(Trabajador)):
                            if Cargo[i]=="Mantenimiento":
                                archivo.write((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*300}\n"))
                
                case "5":
                    with open ("lista_trabajadores.txt", "w") as archivo:
                        for i in range(len(Trabajador)):
                            archivo.write((f"{"="*30}\n Nombre: {Trabajador[i]}\n Puesto: {Cargo[i]}\n Sueldo bruto: {Sueldo_Bruto[i]}\n Descuento salud: {Desc_Salud[i]}\n Descuento AFP: {Desc_AFP[i]}\n Liquidacion a pagar: {Liquido_Pagar[i]}\n{"="*30}\n"))
    
        case "4":
            print("Adios")