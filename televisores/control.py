from televisores.tv import TV
class Control:
    
    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)
    def turnOn(self):
        self.tv.turnOn
        #TV.turnOn
    def turnOff(self):
        self.tv.turnOff
        #TV.turnOff
    def canalUp(self):
        self.tv.canalUp
        #TV.canalUp
    def canalDown(self):
        self.tv.canalDown
        #TV.canalDown
    def volumenUp(self):
        self.tv.volumenUp
        #TV.volumenUp
    def volumenDown(self):
        self.tv.volumenDown
        #TV.volumenDown
    def setCanal(self, can):
        self.tv.setCanal(can)
        #TV.setCanal
    
