import sys
import os
import hashlib
import csv
import socket
import select
import tkinter as tk
import json
import msvcrt
from datetime import datetime
from Chain import *
from AVL import *


#var
arbol = AVL()
cadena = Chain()
indexB = 0
clase = ""
dataA = ""
mensaje = ''
#
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

class Menu:
    

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
            diccionario = json.loads(block)
            indexD = diccionario['INDEX']
            timeD = diccionario['TIMESTAMP']
            classD = diccionario['CLASS']
            dataD = diccionario['DATA']
            previousD = diccionario['PREVIOUSHASH']
            hashD = diccionario['HASH']
            #validar arbol
            dataD2 = json.dumps(dataD)
            if block != '':
                server.sendall(block.encode('utf-8'))    
            msj2 = self.modoEscucha()
            if msj2 != '':
                if msj2 == 'true':
                    cadena.add(indexD,timeD,classD,dataD2,previousD,hashD)
                    global indexB
                    indexB += 1
                    print('SE AGREGO A LA CADENA')
                    self.menuP()
                elif msj2 == 'false':
                    print('NO SE AGREGARA A LA CADENA')
                    self.menuP()
        elif opcion == '2':
            self.selectBloque()
        elif opcion == '3':
            self.menuReportes()
        elif opcion == '4':
            msj = self.modoEscucha()
            if msj != 'true' and msj != 'false':
                diccionario = json.loads(msj.rstrip())
                indexD = diccionario['INDEX']
                timeD = diccionario['TIMESTAMP']
                classD = diccionario['CLASS']
                dataD = diccionario['DATA']
                previousD = diccionario['PREVIOUSHASH']
                hashD = diccionario['HASH']
                #validar arbol
                #valida HASH
                dataD2 = json.dumps(dataD,separators=(',',':'))
                hashT = self.encrypt_string(str(indexD)+timeD+classD+dataD2+previousD)
                print(hashD)
                print(hashT)
                if hashT == hashD:
                    server.sendall('true'.encode('utf-8'))
                else:
                    server.sendall('false'.encode('utf-8'))
                msj = self.modoEscucha()
                if msj == 'true' or msj == 'false':
                    if msj == 'true':
                        cadena.add(indexD,timeD,classD,dataD2,previousD,hashD)
                        print('SE AGREGO A LA CADENA')
                        indexB  += 1
                        self.menuP()
                    elif msj == 'false':
                        print('NO SE AGREGARA A LA CADENA')
                        self.menuP()
        elif opcion == '5':
            sys.exit()
        else:
            self.menuP()    

    def selectBloque(self):
        os.system("cmd /c cls")
        print("############################################################")
        print("###################### SELECT BLOCK ###########################")
        bloqueActual = cadena.head
        if cadena.head is not None:
            print('INDEX: '+bloqueActual.INDEX)
            print('TIMESTAMP: '+bloqueActual.TIMESTAMP)
            print('CLASS: '+bloqueActual.CLASS)
            print('DATA: '+bloqueActual.DATA[0:50])
            print('PREVIOUSHASH: '+bloqueActual.PREVIOUSHASH)
            print('HASH: '+bloqueActual.HASH)
        while self.keypress != '\r':
            if self.keypress == 'xe0':
                bloqueActual = bloqueActual.next
                os.system("cmd /c cls")
                print('INDEX: '+bloqueActual.INDEX)
                print('TIMESTAMP: '+bloqueActual.TIMESTAMP)
                print('CLASS: '+bloqueActual.CLASS)
                print('DATA: '+bloqueActual.DATA[0:50])
                print('PREVIOUSHASH: '+bloqueActual.PREVIOUSHASH)
                print('HASH: '+bloqueActual.HASH)
            if self.keypress == '\r':
                #mandar data al arbol
                arbol.root = None
                #llenar arbol
                self.menuP()


                        
    def keypress(self):    
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                return key
               

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
            self.menuReportes()
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
            self.reportesTree()
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
                
        
           
  
    def crearBloque(self):
        self.bulkL()
        if indexB is 0:
            now = datetime.now()
            timeA = now.strftime("%d-%m-%Y::%H:%M:%S")
            hashN = self.encrypt_string(str(indexB)+timeA+clase+dataA+'0000')
            jsonB = "{\"INDEX\": "+str(indexB)+","+"\"TIMESTAMP\": \""+timeA+"\",\"CLASS\": \""+clase+"\",\"DATA\": "+dataA+",\"PREVIOUSHASH\": \"0000\",\"HASH\": \""+hashN+"\"}"
            return jsonB
        else:
            now = datetime.now()
            timeA = now.strftime("%d-%m-%Y::%H:%M:%S")
            hashN = self.encrypt_string(str(indexB)+timeA+clase+dataA+cadena.end.HASH)
            jsonB = "{\"INDEX\": "+str(indexB)+","+"\"TIMESTAMP\": \""+timeA+"\",\"CLASS\": \""+clase+"\",\"DATA\": "+dataA+",\"PREVIOUSHASH\": \""+cadena.end.HASH+"\",\"HASH\": \""+hashN+"\"}"
            return jsonB


    def encrypt_string(self,string):
        sha_encyption = hashlib.sha256(string.encode()).hexdigest()
        return sha_encyption

    #CLIENTE-SERVIDOR
    def modoEscucha(self):
        global mensaje
        mensaje = ''
        while mensaje is '':
            read_sockets = select.select([server],[],[],1)[0]
            import msvcrt
            if msvcrt.kbhit(): read_sockets.append(sys.stdin)
            for socks in read_sockets:
                if socks == server:
                    message = socks.recv(2048)
                    if message.decode('utf-8') != 'Welcome to [EDD]Blockchain Project!' and message.decode('utf-8') == 'true':
                        mensajeR = message.decode('utf-8')
                        mensaje = mensajeR
                        return mensaje
                    elif message.decode('utf-8') != 'Welcome to [EDD]Blockchain Project!' and message.decode('utf-8') == 'false':
                        mensajeR = message.decode('utf-8')
                        mensaje = mensajeR
                        return mensaje
                    elif message.decode('utf-8') != 'Welcome to [EDD]Blockchain Project!' and message.decode('utf-8') != 'false' and message.decode('utf-8') != 'true':
                        mensajeR = message.decode('utf-8')
                        mensaje = mensajeR
                        return mensaje      
        
    
prueba = Menu()
prueba.menuP()

        




        
