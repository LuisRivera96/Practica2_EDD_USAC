import sys
import os
import hashlib
import csv
import socket
import select
import tkinter as tk
from datetime import datetime
from Chain import*
from AVL import*


#var
arbol = AVL()
cadena = Chain()
indexB = 0
clase = ""
dataA = ""
#

class Menu:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) != 3:
	    print ("Correct usage: script, IP address, port number")
	    exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))

    def menuP(self):
        #os.system("cmd /c cls")
        print("############################################################")
        print("###################### MAIN MENU ###########################")
        print("1. Insert Block")
        print("2. Select Block")
        print("3. Reports")
        print("4. Modo Escucha")
        print("5. Salir")
        opcion = input()
        if opcion  == '1':
            block = self.crearBloque()
            print(block)
            self.keypress() 
        elif opcion == '2':
            print("bloques")
        elif opcion == '3':
            self.menuReportes()
        elif opcion == '4':
            self.modoEscucha()
            
        elif opcion == '5':
            sys.exit()
        else:
            self.menuP()    

    def selectBloque(self):
        os.system("cmd /c cls")
        print("############################################################")
        print("###################### SELECT BLOCK ###########################")
        if self.cadena.head is not None:
            print('INDEX: '+self.cadena.head.INDEX)
            print('TIMESTAMP: '+self.cadena.head.TIMESTAMP)
            print('CLASS: '+self.cadena.head.CLASS)
            print('DATA: '+self.cadena.head.DATA[0:50])
            print('PREVIOUSHASH: '+self.cadena.head.PREVIOUSHASH)
            print('HASH: '+self.cadena.head.HASH)

            
    def keypress(self,event):
        if event.keypress == 'KEY_RIGHT':
            print("derecha")
        elif event.keypress == 'KEY_LEFT':
            print("izquierda")
        elif event.keypress == 'KEY_ENTER':
            print("enter")        
            



    def menuReportes(self):
        os.system("cmd /c cls")
        print("############################################################")
        print("###################### MENU REPORTS ###########################")
        print("1. BlockChain Report")
        print("2. Tree Reports")
        print("3. Regresar")
        opcion = input()
        if opcion  == '1':
            cadena.graphiz()
        elif opcion == '2':
            self.reportesTree()
        elif opcion == '3':
            self.menuP()
        else:
            self.menuReportes()

    def reportesTree(self):
        print("############################################################")
        print("###################### TREE REPORTS ###########################")
        print("1. Visualizar Arbol")
        print("2. Recorridos")
        print("3. Regresar")
        opcion = input()
        if opcion  == '1':
            arbol.getGrafica()
        elif opcion == '2':
            os.system("cmd /c cls")
            print("############################################################")
            print("###################### RECORRIDOS ###########################")
            print("1. Preorden")
            print("2. Inorden")
            print("3. Portorden")
            print("4. Regresar")
            opcion2 = input()
            if opcion2 == '1':
                arbol.getGraphPreo()
                arbol.preorden()
                self.reportesTree()
            elif opcion2 == '2':
                arbol.getGraphIno()
                arbol.inorden()
                self.reportesTree()
            elif opcion2 == '3':
                arbol.getGraphPoso()
                arbol.posorden()
                self.reportesTree()
            elif opcion2 == '4':
                self.reportesTree()
            else:
                self.reportesTree()

        elif opcion == '3':
            self.menuReportes()
        else:
            self.reportesTree()


    def bulkL(self):
        fila = 0
        os.system("cmd /c cls")
        print("#######################INSERTAR BLOQUE##########################")
        print("Ingrese nombre del archivo .csv")
        nombre = input()
        nombreB = "bloques/"+nombre
        datos = []
        with open(nombreB) as csvfile:
            readCSV = csv.reader(csvfile,delimiter=',')
            for row in readCSV:
                  dato = row[1]
                  datos.append(dato)

        global clase
        clase = datos[0]
        global dataA
        dataA = datos[1]        
        print("clase= "+datos[0])
        print("data= "+datos[1]) 
        #self.menuP()    
  
    def crearBloque(self):
        self.bulkL()
        if indexB is 0:
            now = datetime.now()
            timeA = now.strftime("%d-%m-%Y::%H:%M:%S")
            hashN = self.encrypt_string(str(indexB),timeA,clase,dataA,'0000')
            jsonB = "{\"INDEX\": "+str(indexB)+",\n"+"\"TIMESTAMP\": \""+timeA+"\",\n\"CLASS\": \""+clase+"\",\n\"DATA\": "+dataA+",\n\"PREVIOUSHASH\": \"0000\",\n\"HASH\": \""+hashN+"\"\n}"
            return jsonB
        else:
            now = datetime.now()
            timeA = now.strftime("%d-%m-%Y::%H:%M:%S")
            hashN = self.encrypt_string(str(indexB),timeA,clase,dataA,cadena.end.HASH)
            jsonB = "{\"INDEX\": "+str(indexB)+",\n"+"\"TIMESTAMP\": \""+timeA+"\",\n\"CLASS\": \""+clase+"\",\n\"DATA\": "+dataA+",\n\"PREVIOUSHASH\": \""+cadena.end.HASH+"\",\n\"HASH\": \""+hashN+"\"\n}"
            return jsonB


    def encrypt_string(self,string,string2,string3,string4,string5):
        string6 = string+string2+string3+string4,string5
        sha_encyption = hashlib.sha256(str(string6).encode()).hexdigest()
        return sha_encyption

    def modoEscucha(self):
        while True:
            read_sockets = select.select([server],[],[],1)[0]
            import msvcrt
            if msvcrt.kbhit(): read_sockets.append(sys.stdin)

            for socks in read_sockets:
                if socks == server:
                    message = socks.recv(2048)
                    mensaje = message.decode('utf-8')
                    print(mensaje)
        
        



    #CLIENTE-SERVIDOR


prueba = Menu()
prueba.menuP()

        




        
