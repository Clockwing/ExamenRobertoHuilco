from ejercicio6categoria import Categoria

class Productot(Categoria):
  nombre           = str
  fechadecaducidad = str
  categoria  = Categoria("","")
  def __init__(self, nombre,fechadecaducidad, categoria):
    self.nombre           = nombre
    self.fechadecaducidad = fechadecaducidad
    self.categoria        = categoria