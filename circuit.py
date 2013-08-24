class LogicGate(object):
    def __init__(self,name):
        self.label = name
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(raw_input("Enter Pin A input for gate %s -->" % self.label))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB:
            return self.pinB.getFrom().getOutput()
        else:
            return int(raw_input("Enter Pin B input for gate %s -->" % self.label))

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self, name):
        LogicGate.__init__(self,name)
        self.pin = None

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pin")

    def getPin(self):
        if self.pin:
            return self.pin.getFrom().getOutput()
        else:
            return int(raw_input("Enter Pin input for gate %s -->" % self.label))

class AndGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self,name)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a==1 and b==1 else 0

class NandGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 0 if a == 1 and b == 1 else 0
    
class OrGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self,name)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a==1 or b == 1 else 0

class NorGate(BinaryGate):
    def __init__(self, name):
        BinaryGate.__init__(self, name)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return 1 if a==0 and b==0 else 0

class NotGate(UnaryGate):
    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def performGateLogic(self):
        a = self.getPin()
        return 1 if a==0 else 0

class Connector(object):
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

   

    

if __name__ == '__main__':
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g4 = NorGate("G4")
    c1 = Connector(g1, g4)
    c2 = Connector(g2, g4)

    g5 = NandGate('G5')
    g6 = NandGate('G6')
    g7 = AndGate('G7')
    c3 = Connector(g5, g7)
    c4 = Connector(g6, g7)

    


    assert(g4.getOutput() == g7.getOutput())
    print g4.getOutput()
    
   

