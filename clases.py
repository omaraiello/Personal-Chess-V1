class Ficha:

    def __init__(self,tipo,imagen,posicion_X,posicion_Y,valor,color,vivo,TAMANO_CUADRO):
        self.tipo = tipo
        self.imagen = imagen
        self.posicion_X = posicion_X
        self.posicion_Y = posicion_Y
        self.valor = valor
        self.color = color
        self.vivo = vivo
        self.TAMANO_CUADRO = TAMANO_CUADRO
        self.pixel_X = (posicion_X * TAMANO_CUADRO + TAMANO_CUADRO // 2)-25
        self.pixel_Y = (posicion_Y * TAMANO_CUADRO + TAMANO_CUADRO // 2)-25
    
    def debug_print(self):
        print("posicion_X = ",self.posicion_X) 
        print("posicion_Y = ",self.posicion_Y)
        print("Valor = ",self.valor)
        print("Color = ",self.color)
        print("Vivo = ",self.vivo)
        
    def pixel(self):
        self.pixel_X = (self.posicion_X * self.TAMANO_CUADRO + self.TAMANO_CUADRO // 2)-25
        self.pixel_Y = (self.posicion_Y * self.TAMANO_CUADRO + self.TAMANO_CUADRO // 2)-25