import queue

# F.I.F.O
miCola = queue.Queue()

#L.I.F.O
miCola = queue.LifoQueue()

#Priority
miCola = queue.PriorityQueue()

miCola.put((3,"Madrid"))
miCola.put((1,"Bogota"))
miCola.put((2,"Mexico"))

# Sacamos elemento
print(miCola.get())

print("A continuacion se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:
    print(elemento)