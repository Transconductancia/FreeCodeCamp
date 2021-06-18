class persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("estoy avanzando")
        

class ciclista(persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("estoy avanzando en bici")

if __name__=="__main__":
    persona=persona("carlos")
    print(persona.avanza())
    ciclista=ciclista("juan")
    print(ciclista.avanza())
