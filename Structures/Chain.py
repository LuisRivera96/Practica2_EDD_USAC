import os
import subprocess
class Block:
    def __init__(self,INDICE,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH):
        self.INDICE = INDICE
        self.TIMESTAMP = TIMESTAMP
        self.CLASS = CLASS
        self.DATA = DATA
        self.PREVIOUSHASH = PREVIOUSHASH
        self.HASH
        self.next = None
        self.previous = None

class Chain:

    def  __init__(self):
        self.head = None
        self.end = None

    def add(self,INDICE,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH):
        bloque = Block(INDICE,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH)
        if self.head is None:
            self.head = bloque
            self.end = bloque
            self.head.next = None
            self.end.next = None
            self.head.previous = None
            self.end.previous = None
        else:
            self.end.next = bloque
            bloque.previous = self.end
            self.end = bloque
            self.end.next = None

    def buscar(self,CLASS):
        temporal = self.head
        while temporal is None:
            if temporal.CLASS == CLASS:
                return temporal
            temporal = temporal.next    
        
    def graphiz(self):
        if self.head is None:
            print("Cadena Vacia")
        else:
            f = open('Blockchain.dot','w')
            f.write('digraph firsGraph{\n')
            f.write('node [shape=record];\n')
            f.write('rankdir=UD;\n')
            temp = self.head
            count = 0
            while temp.next is not None:
                f.write('node{} [label=\"Class = {}'+'\\n'+'TimeStamp={}'+'\\n'+'PHASH={}'+'\\n'+'HASH={} \"];\n'.format(count,temp.CLASS,temp.TIMESTAMP,temp.PREVIOUSHASH,temp.HASH))
                count+=1
                f.write('node{} -> node{};\n'.format(count-1,count))
                f.write('node{} -> node{};\n'.format(count,count-1))
                temp = temp.next
            f.write('node{} [label=\"Class = {}'+'\\n'+'TimeStamp={}'+'\\n'+'PHASH={}'+'\\n'+'HASH={} \"];\n'.format(count,temp.CLASS,temp.TIMESTAMP,temp.PREVIOUSHASH,temp.HASH))
            f.write('}')
            f.close()
            os.system('dot Blockchain.dot -Tpng -o Blockchain.png')
            os.system('Blockchain.png')







                

        
    