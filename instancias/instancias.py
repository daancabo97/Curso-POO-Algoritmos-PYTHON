# Calcular distancias entre dos coordenadas

class Coordenada:
  
    def __init__(self, x ,y ):                         # METODO INIT 
        self.x = x
        self.y = y
                                                       
    def distancia(self, otra_coordenada):              # METODO QUE DEFINE LA DISTANCIA ENTRE DOS COORDENADAS
        x_diff = (self.x - otra_coordenada.x)**2       #  INSTANCIA ENTRE UNA COORDENADA X Y OTRA COORDENADA SU X
        y_diff = (self.y - otra_coordenada.y)**2       #  INSTANCIA ENTRE UNA COORDENADA X Y OTRA COORDENADA SU Y 

        return (x_diff + y_diff)**0.5                  # RETORNA EL VALOR DE LA RAIZ CUADRADA DE ESTAS DISTANCIAS AL CUADRADO

if __name__ == '__main__':                             
     coor_1 = Coordenada(3 , 30)                       # GENERAR UNA INSTANCIA DE LA PRIMERA COORDENADA
     coor_2 = Coordenada(4 , 8)                        # GENERAR UNA INSTANCIA DE LA SEGUNDA COORDENADA

     print(coor_1.distancia(coor_2))                   # SABER DISTANCIA ENTRE LAS DOS COORDENADAS 
     print(isinstance(coor_2,Coordenada))              # ISINSTANCE : DETERMINA SI ALGUNA DE ESTAS CORRDENADAS ES INSTANCIA DE LA CLASE Coordenada

