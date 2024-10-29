class Suma :
    def suma (self):
        pass
class Numeros (Suma ):
    def suma (self):
        print (5+7)
class Listas (Suma ):
    def suma (self):
        print ([5,7, "frankcoise"] + ["daniel", 43])
class Cadena (Suma):
    def suma (self):
        frank= "fran"
        coise= "coise"
        print (frank + coise )
        
for Suma in Numeros(), Listas (), Cadena ():
    Suma.suma ()