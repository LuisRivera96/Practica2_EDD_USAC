import sys
class Menu:
    def menuP(self):
        print("############################################################")
        print("###################### MAIN MENU ###########################")
        print("1. Insert Block")
        print("2. Select Block")
        print("3. Reports")
        print("4. Salir")
        opcion = input()
        if opcion  == 1:
            #crear bloque
            #verificar
            #validar
            #insertar
        elif opcion == 2:
            print("bloques")
        elif opcion == 3:
            #llamar menu reportes
            print("Reportes")
        elif opcion == 4:
            sys.exit()
        else:
            self.menuP()      
        
