superheroes = [
    "Spider-Man", "Iron Man", "Capitan America", "Thor",
    "Hulk", "Black Widow", "Hawkeye", "Black Panther",
    "Doctor Strange", "Wolverine", "Storm", "Deadpool",
    "Ant-Man", "Wasp", "Falcon"
]

### PUNTO 1 ###

def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    
    if lista[indice] == "Capitan America":
        return True
    
    return buscar_capitan_america(lista, indice + 1)

### PUNTO 2 ###

def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return   
    print(f"{indice + 1}. {lista[indice]}")
    listar_superheroes(lista, indice + 1)

### IMPLEMENTACIONES ###

if buscar_capitan_america(superheroes):
    print ('Capitan america esta en la lista')
else:
    print ('Capitan america no esta en la lista')
    
listar_superheroes(superheroes)

############################################################################################



