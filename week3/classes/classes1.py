class myClass:
    def __init__(self):
        self.text = ''
    def getString(self):
        self.text = str(input())
    def printString(self):
        print(self.text.upper())
c = myClass()
c.getString()
c.printString()