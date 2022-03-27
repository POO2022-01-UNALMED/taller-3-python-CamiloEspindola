from televisores.tv import TV
class Control:
    
    def enlazar(self, tv):
        self.tv = tv
        # tv.setControl(self)
    def turnOn(self):
        tv.turnOn()
    # def turnOff(self):
    #     TV.turnOff()
    # def canalUp(self):
    #     TV.canalUp()
    # def canalDown(self):
    #     TV.canalDown()
    # def volumenUp(self):
    #     TV.volumenUp()
    # def volumenDown(self):
    #     TV.volumenDown()
    # def setCanal(self):
    #     TV.setCanal()
    
tv1 = TV('marca1', True)

# control1 = Control()
# control1.enlazar(tv1)
# control1.turnOn()
