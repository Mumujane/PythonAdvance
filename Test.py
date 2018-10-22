class MyMath(object):
    def __init__(self):
        self.__PI = [3.141592658]

    @property
    def PI(self):
        return self.__PI


mymath = MyMath()

print(type(mymath.PI))

print(mymath.PI.append(123))
print(mymath.PI)
###123###123###123###123###hlsad###123###hlsad###123###hlsad###123###hlsad###123###hlsad###123###hlsad###123###hlsad