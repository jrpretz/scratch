import types

class Getter:
    def __init__(self,column):
        self.column = column
    def __call__(self,instance):
        return instance.data[self.column]

class Setter:
    def __init__(self,column):
        self.column = column
    def __call__(self,instance,value):
        instance.data[self.column] = value

class Toy:
    def __init__(self):
        self.data = [0] * 3
        self.data[0] = 0
        self.data[1] = 1
        self.data[2] = 2

        for i in range(0,3):
            setattr(self,'get_%02d'%(i),types.MethodType(Getter(i),self))
            setattr(self,'set_%02d'%(i),types.MethodType(Setter(i),self))



t = Toy()
print t.get_01()
print t.get_02()
t.set_02(45)
print t.get_02()
