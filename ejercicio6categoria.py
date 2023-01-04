from ejercicio6seccion import Seccion

class Categoria(Seccion):
  nombre = str
  seccion = ("","")
  
  def __init__(self, nombre, seccion):
    self.nombre  = nombre
    self.seccion = seccion