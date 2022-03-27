class TV:
    numTV = 0
        
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        control = None
        TV.numTV+=1
    
    
    #Tendrá los métodos set y get para los atributos marca, control, precio, volumen y canal.
    # setters
    def setMarca(self, mar):
        self.marca = mar
    def setControl(self, con):
        self.control = con
    def setPrecio(self, pre):
        self.precio = pre
    def setVolumen(self, vol):
        if(self.estado == True and vol<=7 and vol >=0):
            self.volumen = vol
    def setCanal(self, can):
        if(self.estado == True and can>0 and can<=120):
            self.canal = can
    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num    
    
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
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    def getEstado(self):
        return self.estado
    #funciones 
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def canalUp(self):
        if(self.estado == True and self.canal<120):
            self.canal+=1
    def canalDown(self):
        if(self.estado == True and self.canal>1):
            self.canal-=1
    def volumenUp(self):
        if(self.estado == True and self.volumen<7):
            self.volumen+=1
    def volumenDown(self):    
        if(self.estado == True and self.volumen>=1):
            self.volumen-=1 