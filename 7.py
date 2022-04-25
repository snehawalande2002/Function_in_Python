#   function return another function

def Arundhati():
    print("I am Arundhati")
def Sneha():
    return Arundhati
a = Sneha()
a()