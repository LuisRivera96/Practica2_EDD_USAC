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
        self.root = self.addRecursived(self.root,CARNET,NAME)

    def addRecursived(self,ROOT,CARNET,NAME):
        if ROOT is None:
            nuevo = nodeAVL(CARNET,NAME)
            return nuevo
        if CARNET < ROOT.CARNE:
            ROOT.LEFT = self.addRecursived(ROOT.LEFT,CARNET,NAME)
        if CARNET > ROOT.CARNE:
            ROOT.RIGHT = self.addRecursived(ROOT.RIGHT,CARNET,NAME)      

        ROOT.ALTURA = 1 + max(self.getHeight(ROOT.LEFT),self.getHeight(ROOT.RIGHT))
        balance = self.getBalance(ROOT)

        if balance > 1 and CARNET < ROOT.LEFT.CARNE:
            return self.rightRotate(ROOT)

        if balance < -1 and CARNET > ROOT.RIGHT.CARNE:
            return self.leftRotate(ROOT)

        if balance > 1 and CARNET > ROOT.LEFT.CARNE:
            ROOT.LEFT = self.leftRotate(ROOT.LEFT)
            return self.rightRotate(ROOT)

        if balance < -1 and CARNET < ROOT.RIGHT.CARNE:
            ROOT.RIGHT = self.rightRotate(ROOT.RIGHT)
            return self.leftRotate(ROOT)

        return ROOT
            
                   


    
    def leftRotate(self,z):
        y = z.RIGHT
        T2 = y.LEFT
        y.LEFT = z
        z.RIGHT = T2
        z.ALTURA = 1 + max(self.getHeight(z.LEFT),self.getHeight(z.RIGHT))
        y.ALTURA = 1 + max(self.getHeight(y.LEFT),self.getHeight(y.RIGHT))
        return y

    
    def rightRotate(self,z):
        y = z.LEFT
        T3 = y.RIGHT
        y.RIGHT = z
        z.LEFT = T3
        z.ALTURA = 1 + max(self.getHeight(z.LEFT),self.getHeight(z.RIGHT))
        y.ALTURA = 1 + max(self.getHeight(y.LEFT),self.getHeight(y.RIGHT))
        return y

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


    def balanced(self,ROOT):
        if ROOT is not None:
            self.balanced(ROOT.LEFT)
            if self.getBalance(ROOT) > 1 or self.getBalance(ROOT) < -1:
                return FalseS
            self.balanced(ROOT.RIGHT)        

    #RECORRIDOS
    #########################INORDEN#########################
    inor = "INICIO-> "
    def inorden(self):
        self.inordenR(self.root)
    def inordenR(self,ROOT):
        if ROOT is not None:
            self.inordenR(ROOT.LEFT)
            inor = inor + ROOT.CARNE + "-" + ROOT.NAME + "-> "
            self.inordenR(ROOT.RIGHT)
        inor = inor + " ->FIN"    
        print(inor)

    def gInorden(self,ROOT):
        DotInor = ""
        if ROOT is not None:
            DotInor = DotInor + self.gInorden(ROOT.LEFT)
            DotInor = DotInor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +" "+ROOT.NAME+"\"];\n"
            DotInor = DotInor + self.gInorden(ROOT.RIGHT)
        return DotInor

    def getGraphIno(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Inorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gInorden(self.root)
        Dot = Dot + "}"
        f = open('INORDEN.dot','w')
        f.write(Dot)
        f.close()    
        os.system('dot INORDEN.dot -Tpng -o INORDEN.png')
        os.system('INORDEN.png')

    ##############################################################
    #########################PREORDEN#########################
    pre = "INICIO-> "
    def preorden(self):
        self.preordenR(self.root)
    def preordenR(self,ROOT):
        if ROOT is not None:
            pre = pre + ROOT.CARNE + "-" + ROOT.NAME + "-> "
            self.preordenR(ROOT.LEFT)
            self.preordenR(ROOT.RIGHT)
        pre = pre + " ->FIN"    
        print(pre)

    def gPreorden(self,ROOT):
        DotPreor = ""
        if ROOT is not None:
            DotPreor = DotPreor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +" "+ROOT.NAME+"\"];\n"
            DotPreor = DotPreor + self.gPreorden(ROOT.LEFT)
            DotPreor = DotPreor + self.gPreorden(ROOT.RIGHT)
        return DotPreor

    def getGraphPreo(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Preorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gPreorden(self.root)
        Dot = Dot + "}"
        f = open('PREORDEN.dot','w')
        f.write(Dot)
        f.close()    
        os.system('dot PREORDEN.dot -Tpng -o PREORDEN.png')
        os.system('PREORDEN.png')

    ##############################################################
    #########################POSTORDEN#########################
    pos = "INICIO-> "
    def posorden(self):
        self.posordenR(self.root)
    def posordenR(self,ROOT):
        if ROOT is not None:
            self.posordenR(ROOT.LEFT)
            self.posordenR(ROOT.RIGHT)
            pos = pos + ROOT.CARNE + "-" + ROOT.NAME + "-> "
        pos = pos + " ->FIN"    
        print(pos)

    def gPosorden(self,ROOT):
        DotPosor = ""
        if ROOT is not None:
            DotPosor = DotPosor + self.gPosorden(ROOT.LEFT)
            DotPosor = DotPosor + self.gPosorden(ROOT.RIGHT)
            DotPosor = DotPosor + ROOT.CARNE + "[label=\""+ ROOT.CARNE +" "+ROOT.NAME+"\"];\n"
        return DotPosor

    def getGraphPoso(self):
        Dot = ""
        Dot = Dot + "digraph BLOCK{\n"
        Dot = Dot + "label=\"Postorden\";\n"
        Dot = Dot + "rankdir=\"LR\";\n"
        Dot = Dot + self.gPosorden(self.root)
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
                Dot = Dot + str(ROOT.CARNE) + "[label=\" <N " + str(ROOT.CARNE)+ " " + ROOT.NAME + " I> | <f" + str(ROOT.CARNE) + "> " + str(ROOT.CARNE) + "\\n" + " | <f" + str(ROOT.CARNE) + "D> \" shape=\"record\"];\n"
            else:
                Dot = Dot + str(ROOT.CARNE) + ":f " + str(ROOT.CARNE) + "[id=" + str(ROOT.CARNE) + ", color=\"blue\" shape=\"rectangle\"]; \n"

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

                






