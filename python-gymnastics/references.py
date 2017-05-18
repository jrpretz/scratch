

class MyData:
    def __init__(self,x):
        self.x = x

a = MyData(5)
b = a

if b is a:
    print "same, expect same"
else:
    print "same, expect not same"

c = MyData(5)


if b is c:
    print "same, expect not same"
else:
    print "not same, expect not same"


print id(a)
print id(b)
print id(c)
