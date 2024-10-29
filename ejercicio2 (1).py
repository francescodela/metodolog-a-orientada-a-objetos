class Vehiculo:
    def __init__(self, marca, modelo, placa ):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
    def ejercitar (self):
        pass
    def frenar (self):
        pass
    def acelerar (self):
        pass
    def reproducirMusica  (self):
        pass
class Carro (Vehiculo):
    def acelerar (self):
        print (f" el {carro.marca } esta acelerando")
    def frenar (self):
         print (f" el {carro.marca } esta frenando")

    def reproducirMusica  (self):
        print (f" el {carro.marca } esta reproduciendo musica  ")
    
        
class Bicicleta (Vehiculo):
    def ejercitar (self):
        print ( f" la bicicleta {bicicleta.marca} esta ejercitandote" )
    def frenar (self):
        print (f" la bicicleta {bicicleta.marca } esta frenando   ")
        
        
bicicleta= Bicicleta("rogelio", 252,"indefinida ")
carro = Carro ("mustan", 94, "cxdyv2")


carro.reproducirMusica()
carro.frenar()
carro.acelerar()
bicicleta.ejercitar()
bicicleta.frenar()


    
    
        