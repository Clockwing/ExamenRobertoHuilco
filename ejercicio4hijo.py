from ejercicio4padre import Categoria

class Productot(Categoria):
  nombre           = str
  fechadecaducidad = str
  categoria  = Categoria("")
  def __init__(self, nombre,fechadecaducidad, categoria):
    self.nombre           = nombre
    self.fechadecaducidad = fechadecaducidad
    self.categoria        = categoria
    
    
    
if __name__=="__main__":
  
  herenciaarchoivos = Productot("leche", "13-13,2023", Categoria("LActeo"))
  print(vars(herenciaarchoivos))
  print(vars(herenciaarchoivos.categoria))