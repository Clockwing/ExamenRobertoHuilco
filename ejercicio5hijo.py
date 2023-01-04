from ejercicio4hijo import Productot
from ejercicio4padre import Categoria

class Venda(Productot):
  tipo     = str
  total    = str
  producto = ("","","")
  def __init__(self, tipo, total, producto):
    self.tipo       = tipo
    self.total      = total
    self.prproducto = producto
    
if __name__=="__main__":
    
 ejercicio5 = Venda("Tarjeta", "20", Productot("Leche", "02-03-2013", Categoria("Lacteo")))
   
 print(vars(ejercicio5))
 print(vars(ejercicio5.prproducto))
 print(vars(ejercicio5.prproducto.categoria))

 
