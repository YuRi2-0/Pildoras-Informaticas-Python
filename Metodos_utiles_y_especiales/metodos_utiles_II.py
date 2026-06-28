# import datetime

# hoy = datetime.date.today()

# el metodo __repr__ es mas precisa que __str__
# print(repr(hoy))

class Agenda():
    
    def __init__(self):
        self.miAgenda={}
        
    def agregarPersonas(self,nombre,telefono):
        self.miAgenda[nombre]=telefono

    def __len__(self):
        
        return len(self.miAgenda)

agendaPersonal= Agenda()

agendaPersonal.agregarPersonas("Juan",'1234433')
agendaPersonal.agregarPersonas("Maria",'736736')

print(len(agendaPersonal))
