sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
#Para crear diccionarios, se usan llaves "{}" y se escriben los datos del diccionario.
#Si son alabras deben ser escritas entre comillas y separadas por comas, pero si son números no se escriben entre comillas y se separan por comas.
#También se le puede asignar algún argumento a cada dato, colocando ":" después del dato y enseguida colocamos el argmuneto de ese dato; también se 
#separa por comas
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
print(subtotal_to_total)

students_in_classes = {"Diseño de Software": ["Aaron", "Delila", "Samson"], "Cartografía": ["Christopher", "Juan", "Marco"], "Filosofía": ["Frederica", "Manuel"], "Ingeniería": "Daniel", "Edad":20}
print(students_in_classes)

Diccionario_prueba = {}
Diccionario_prueba["Nota"]=5
print(Diccionario_prueba)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
oscar_winners["Animated Feature"] = "Wall-E"
print(oscar_winners)

Bebidas = ["espresso","chai","decaf","drip"]
Cafeina = [60,40,0,120]
zipped_Bebidas = zip(Bebidas,Cafeina)
Bebidas_a_Cafeina = {key:value for key, value in zipped_Bebidas}
print(Bebidas_a_Cafeina)
