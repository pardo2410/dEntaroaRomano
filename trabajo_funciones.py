def doble(n):
    return n*2

class persona():
    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad
    def __repr__(self):
        return 'Me llamo {} y tengo {} annos'.format(self.name,self.age)
    def dimequieneres(self):
        return self.__repr__()


luis = persona('Luis',19)
mon = persona('Ramon',50)
print(luis.dimequieneres())
print(doble(self.edad))
print(luis.double(self.edad))

