import os
import subprocess
class nodeAVL:
    def __init__(self,CARNE,NAME):
        self.CARNE = CARNE
        self.NAME = NAME
        self.ALTURA = 1
        self.FE = 0
        self.RIGHT = None
        self.LEFT = None

class AVL:
    def __init__(self):
        self.root = None

    def add(self,CARNET,NAME):
        if self.root is not None:
            return self.addRecursived(self.root,CARNET,NAME)
        else:
            nuevo = nodeAVL(CARNET,NAME)
            self.root = nuevo    
        

    def addRecursived(self,ROOT,CARNET,NAME):
        if CARNET < ROOT.CARNE:
            if ROOT.LEFT is not None:
                self.addRecursived(ROOT.LEFT,CARNET,NAME)
            else:
                nuevo = nodeAVL(CARNET,NAME)
                ROOT.LEFT = nuevo
        elif CARNET > ROOT.CARNE:
            if ROOT.RIGHT is not None:
                self.addRecursived(ROOT.RIGHT,CARNET,NAME)
            else:
                nuevo = nodeAVL(CARNET,NAME)
                ROOT.RIGHT = nuevo
        else:
            print("Ya Ingresado")                        


    def getHeight(self,RAIZ):
        if RAIZ is None:
            return 0
        return RAIZ.ALTURA 

    def getBalance(self,RAIZ):
        if RAIZ is None:
            return 0
        return self.getHeight(RAIZ.LEFT) - self.getHeight(RAIZ.RIGHT)              

    #BUSQUEDA
    def Busqueda(self,CARNE):
        return self.BusquedaR(self.root,CARNE)
    def BusquedaR(self,ROOT,CARNE):
        if ROOT is None:
            return None
        elif CARNE == ROOT.CARNE:
            return ROOT
        elif CARNE < ROOT.CARNE:
            return self.BusquedaR(ROOT.LEFT,CARNE)
        elif CARNE > ROOT.CARNE:
            return self.BusquedaR(ROOT.RIGHT,CARNE)


        

    #RECORRIDOS
    #########################INORDEN#########################
    
    def inorden(self):
        inor = ""
        self.inordenR(self.root,inor) 
    def inordenR(self,ROOT,CADENA):
        if ROOT is not None:
            self.inordenR(ROOT.LEFT,CADENA)
            CADENA =  ROOT.CARNE + "-" + ROOT.NAME + "-> "
            print(CADENA,end="")
            self.inordenR(ROOT.RIGHT,CADENA)
             

    def gInorden(self,ROOT):
        DotInor = ""
        if ROOT is not None:
            DotInor = DotInor + self.gInorden(ROOT.LEFT)
            DotInor = DotInor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +"\\n"+ROOT.NAME+"\"];\n"
            DotInor = DotInor + self.gInorden(ROOT.RIGHT)
        return DotInor

    def gInordenEnla(self,ROOT):
        DotInor = ""
        if ROOT is not None:
            DotInor = DotInor + self.gInordenEnla(ROOT.LEFT)
            DotInor = DotInor + ROOT.CARNE + ";\n"
            DotInor = DotInor + ROOT.CARNE + " -> "    
            DotInor = DotInor + self.gInordenEnla(ROOT.RIGHT)
        return DotInor

    def getGraphIno(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Inorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gInorden(self.root) 
        Dot = Dot + self.gInordenEnla(self.root)
        Dot = Dot + "}"
        f = open('INORDEN.dot','w')
        f.write(Dot)
        f.close()    
        os.system('dot INORDEN.dot -Tpng -o INORDEN.png')
        os.system('INORDEN.png')

    ##############################################################
    #########################PREORDEN#########################
    
    def preorden(self):
        pre = ""
        self.preordenR(self.root,pre) 
        
    def preordenR(self,ROOT,CADENA):
        if ROOT is not None:
            CADENA =   ROOT.CARNE + "-" + ROOT.NAME + "-> "
            print(CADENA,end="")
            self.preordenR(ROOT.LEFT,CADENA)
            self.preordenR(ROOT.RIGHT,CADENA)   
        

    def gPreorden(self,ROOT):
        DotPreor = ""
        if ROOT is not None:
            DotPreor = DotPreor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +"\\n"+ROOT.NAME+"\"];\n"
            DotPreor = DotPreor + self.gPreorden(ROOT.LEFT)
            DotPreor = DotPreor + self.gPreorden(ROOT.RIGHT)
        return DotPreor

    def gPreordenEnla(self,ROOT):
        DotPreor = ""
        if ROOT is not None:
            DotPreor = DotPreor + ROOT.CARNE + ";\n"
            DotPreor = DotPreor + ROOT.CARNE + " -> "
            DotPreor = DotPreor + self.gPreordenEnla(ROOT.LEFT)
            DotPreor = DotPreor + self.gPreordenEnla(ROOT.RIGHT)
        return DotPreor
        

    def getGraphPreo(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Preorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gPreorden(self.root) 
        Dot = Dot + self.gPreordenEnla(self.root)
        Dot = Dot + "}"
        f = open('PREORDEN.dot','w')
        f.write(Dot)
        f.close()    
        os.system('dot PREORDEN.dot -Tpng -o PREORDEN.png')
        os.system('PREORDEN.png')

    ##############################################################
    #########################POSTORDEN#########################
    
    def posorden(self):
        pos = ""
        self.posordenR(self.root,pos)

    def posordenR(self,ROOT,CADENA):
        if ROOT is not None:
            self.posordenR(ROOT.LEFT,CADENA)
            self.posordenR(ROOT.RIGHT,CADENA)
            CADENA =  ROOT.CARNE + "-" + ROOT.NAME + "-> "
            print(CADENA,end="")  
        

    def gPosorden(self,ROOT):
        DotPosor = ""
        if ROOT is not None:
            DotPosor = DotPosor + self.gPosorden(ROOT.LEFT)
            DotPosor = DotPosor + self.gPosorden(ROOT.RIGHT)
            DotPosor = DotPosor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +"\\n"+ROOT.NAME+"\"];\n"
        return DotPosor

    def gPosordenEnla(self,ROOT):
        DotPosor = ""
        if ROOT is not None:
            DotPosor = DotPosor + self.gPosordenEnla(ROOT.LEFT)
            DotPosor = DotPosor + self.gPosordenEnla(ROOT.RIGHT)
            DotPosor = DotPosor + ROOT.CARNE + ";\n"
            DotPosor = DotPosor + ROOT.CARNE + " -> "
        return DotPosor


    def getGraphPoso(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Postorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gPosorden(self.root) 
        Dot = Dot + self.gPosordenEnla(self.root)
        Dot = Dot + "}"
        f = open('POSORDEN.dot','w')
        f.write(Dot)
        f.close()    
        os.system('dot POSORDEN.dot -Tpng -o POSORDEN.png')
        os.system('POSORDEN.png')

    ##############################################################
    #GRAPHIZAVL

    def graficar(self,ROOT):
        Dot = ""
        if ROOT is not None:
            if ROOT.RIGHT is not None or ROOT.LEFT is not None:
                Dot = Dot + str(ROOT.CARNE) + ":f" + str(ROOT.CARNE) + "[id=" + str(ROOT.CARNE) + ", color=\"blue\"]; \n"
                Dot = Dot + str(ROOT.CARNE) + "[label=\" <N " + str(ROOT.CARNE)+ " I> | <f" + str(ROOT.CARNE) + "> " +"Carne: " +str(ROOT.CARNE)+ "\\n" + "Nombre: "+ROOT.NAME + "\\n" + "Altura: "+str(ROOT.ALTURA) + "\\n" + "FE: "+str(ROOT.FE)   + " | <f" + str(ROOT.CARNE) + "D> \" shape=\"record\"];\n"
            else:
                Dot = Dot + str(ROOT.CARNE) + ":f " + str(ROOT.CARNE) + "[label=\"" +"Carne: " +str(ROOT.CARNE)+ "\\n" + "Nombre: "+ROOT.NAME + "\\n" + "Altura: "+str(ROOT.ALTURA) + "\\n" + "FE: "+str(ROOT.FE) + "\", color=\"blue\" shape=\"rectangle\"]; \n"

            a = self.graficar(ROOT.LEFT)
            if a is not "":
                Dot = Dot + "\"" + str(ROOT.CARNE) + "\" : N" + str(ROOT.CARNE) + "I -> "
                Dot = Dot + " " + a
            b = self.graficar(ROOT.RIGHT)
            if b is not "":
                Dot = Dot + "\"" + str(ROOT.CARNE) + "\" : f" + str(ROOT.CARNE) + "D -> "
                Dot = Dot + " " + b
        return Dot    

    def getGrafica(self):
        dot = ""
        dot = dot + "digraph AVL{\n"
        dot = dot + "compound=true;\n"
        dot = dot + "node[shape=\"Mrecord\"];\n"
        dot = dot + self.graficar(self.root)
        dot = dot + "}"
        f = open('AVL.dot','w')
        f.write(dot)
        f.close()    
        os.system('dot AVL.dot -Tpng -o AVL.png')
        os.system('AVL.png')        

                








