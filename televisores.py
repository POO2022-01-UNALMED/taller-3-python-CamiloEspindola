from http.client import PRECONDITION_FAILED
from mailbox import NoSuchMailboxError
from operator import truediv
from xml.etree.ElementTree import canonicalize


class Marca:
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setNombre(self, nom):
        self.nombre = nom
class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        canal = 1
        volumen = 1
        precio = 500
        self.control
        numTV+=1
    
    
    #Tendrá los métodos set y get para los atributos marca, control, precio, volumen y canal.
    # setters
    def setMarca(self, mar):
        self.marca = mar
    def setControl(self, con):
        self.control = con
    def setPrecio(self, pre):
        self.precio = pre
    def setVolumen(self, vol):
        if(self.estado == True and self.volumen<=7 and self.volumen >=0):
            self.volumen = vol
    def setCanal(self, can):
        if(self.estado == True and self.canal>0 and self.canal<=120):
            self.canal = can
    @staticmethod
    def setNumTV(self, num):
        NumTv = num    
    
    #getters
    def getMarca(self):
        return self.marca
    def getControl(self):
        return self.control
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getCanal(self):
        return self.canal
    @staticmethod
    def getNumTV(self):
        return self.numTV
    def getEstado(self):
        return self.estado
    #funciones 
    def turnOn(self):
        estado = True
    def turnOff(self):
        estado = False
    def canalUp(self):
        if(self.estado == True and canal<120):
            canal+=1
    def canalDown(self):
        if(self.estado == True and canal>1):
            canal-=1
    def volumenUp(self):
        if(self.estado == True and volumen<7):
            volumen+=1
    def volumenDown(self):    
        if(self.estado == True and volumen>=1):
            volumen-=1 

class Control:
    
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)
    def turnOn(self):
        TV.turnOn
    def turnOff(self):
        TV.turnOff
    def canalUp(self):
        TV.canalUp
    def canalDown(self):
        TV.canalDown
    def volumenUp(self):
        TV.volumenUp
    def volumenDown(self):
        TV.volumenDown
    def setCanal(self):
        TV.setCanal



