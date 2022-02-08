class Automovil:
    

    def __init__(self , modelo , marca , color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "En reposo"
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyectaGasolina(10) #
        else:
            self._motor.inyectaGasolina(3) # 

class Motor:

    def __init__(self, cilindros , tipo='gasolina',nivel_gasolina=46000):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.nivel_gasolina = nivel_gasolina

    #
    def inyectaGasolina(self,cantidad): 
        self.nivel_gasolina = self.nivel_gasolina - cantidad

    def temperatura (self, grados ):
        self._temperatura = self._temperatura + grados


    def informacion (self):
       
         print('\n\n')
         print(f'nivel de gasolina = {self.nivel_gasolina}')
         print(f'nivel de temperatura = {self._temperatura}')
         print(f'{car1}')



if __name__ == "__main__":

    car1 = Automovil("AAFF","toyota", "rojo")
    car1._motor.informacion() 
    car1.acelerar("lenta")
    
#######################################################################################################################
print("\n\n")

class Automovil:
    def  __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color 
        self._estando = "en_reposo"
        self._motor = Motor(cilindros = 4) #esto es una  variable privada, por eso se empieza con _
        self._seguridad = AirBag ()

    def acelerar (self, tipo ):
        if tipo == "rapida":
            self._motor.inyectaGasolina(10) # Inyec
            self._motor.temperatura(12)     # Temperatura
        else: 
            self._motor.inyectaGasolina(3)  # Inyec
            self._motor.temperatura(7)      # Temperatura
        self._estado = "EnMovimiento"

    def desAcelerar (self, tipo ):

        if tipo == "brusca":
            self._seguridad.activar()       # Activar
        else:
            pass
            
class Motor:
    def __init__(self, cilindros, tipo = 'gasolina', nivelGasolina = 46000, temperatura = 0 ): #tipo es un parametro ya definido, se le llama default keyword, se entiende comoo un parametro por defecto.
        self.cilindros = cilindros
        self.tipo = tipo 
        self.nivelGasolina = nivelGasolina
        self.estadoTemperatura = temperatura

    # Inyec
    def inyectaGasolina(self, cantidadGasolina):
        self.nivelGasolina = self.nivelGasolina - cantidadGasolina

    # Temperatura
    def temperatura (self, grados ):
        self.estadoTemperatura = self.estadoTemperatura + grados

    def informacion (self): #Esta funcion es temporal, solo para revisar que todo esta funcionanndo :v xd 
        print("\n")
        print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.estadoTemperatura}")
        print("\n")

class AirBag:

    def __init__(self, estado = "optimo"):
        self.estado = estado

    # Activar
    def activar(self):
        print("SISTEMA DE SEGURAD DE CHOQUES ACTIVADO")
        self.estado = "inhalitado"

if __name__ == "__main__":

    car1 = Automovil("AAFF","toyota", "rojo")
    car1._motor.informacion() 
    car1.acelerar("lenta")
    car1._motor.informacion()
    car1.desAcelerar("brusca")
    
print("\n\n")

    


    

  