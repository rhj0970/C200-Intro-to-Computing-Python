class Convergence:
    wheels = 4
    def __init__(self, MAKE, MODEL):
        self.make = MAKE
        self.model = MODEL
        self.blutooth = True
    def getname(self):
        return self.make + " " +self.model
    def getbluetooth(self):
        return self.blutooth
    def setbluetooth(self, onoff):
        self.blutooth = onoff
        

c1 = Convergence("honda", "accord")
c2 = Convergence("BMW", "5series")
print(c1.wheels)

print(c2.wheels)
Convergence.wheels = 8
c2.setbluetooth(False)

print(c1.getname())

print(c1.getbluetooth())
print(c1.wheels)
print(c2.getname())
print(c2.getbluetooth())
print(c2.wheels)

