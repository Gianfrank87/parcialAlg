from super_heroes_data import superheroes
from list_ import List
from Myqueue import Queue


def order_by_name(item):
    return item.name

class Superhero:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name} - {'Villano' if self.is_villain else 'Héroe'}"

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)

for data in superheroes:
    hero = Superhero(
        name=data["name"],
        alias=data["alias"],
        real_name=data["real_name"],
        short_bio=data["short_bio"],
        first_appearance=data["first_appearance"],
        is_villain=data["is_villain"],
    )
    list_superhero.append(hero)

list_superhero.sort_by_criterion('name')

print("Listado de superhéroes ordenado por nombre:")
list_superhero.show()

print('*************************************************************')


pos_thing = list_superhero.search('The Thing', 'name')
if pos_thing is not None:
    print(f"The Thing está en la posición: {pos_thing}")
else:
    print("The Thing no está en la lista")


pos_rocket = list_superhero.search('Rocket Raccoon', 'name')
if pos_rocket is not None:
    print(f"Rocket Raccoon está en la posición: {pos_rocket}")
else:
    print("Rocket Raccoon no está en la lista")

print('*************************************************************')

print("Listado de villanos:")

for hero in list_superhero:
    if hero.is_villain:
        print(hero)

print ('************************************************************')

villain_queue = Queue()

for hero in list_superhero:
    if hero.is_villain:
        villain_queue.arrive(hero)

print("Villanos que aparecieron antes de 1980:")

size = villain_queue.size()

for _ in range(size):
    villain = villain_queue.attention()
    if villain.first_appearance < 1980:
        print(villain)
        villain_queue.arrive(villain)

print ('************************************************************')

prefijos = ['Bl', 'G', 'My', 'W']

print("Superhéroes cuyos nombres comienzan con Bl, G, My o W:")

for hero in list_superhero:
    if any(hero.name.startswith(prefijo) for prefijo in prefijos):
        print(hero)

print ('************************************************************')

print("\n6. Personajes ordenados por nombre real:")

lista_real = List()

lista_real.add_criterion('real_name', lambda x: getattr(x, 'real_name', "") or "")


for personaje in list_superhero:
    lista_real.append(personaje)

lista_real.sort_by_criterion('real_name')

lista_real.show()
print ('*************************************************************')

def order_by_first_appearance(item):
    return item.first_appearance

list_superhero.add_criterion('first_appearance', order_by_first_appearance)

list_superhero.sort_by_criterion('first_appearance')

print("Listado de superhéroes ordenado por fecha de aparición:")
list_superhero.show()

print ('**************************************************************')

for hero in list_superhero:
    if hero.name == "Ant Man":
        hero.real_name = "Scott Lang"
        print(f"Nombre real de {hero.name} modificado a {hero.real_name}")
        break

print ('**************************************************************')

print("Personajes cuya biografía incluye 'time-traveling' o 'suit':")

for hero in list_superhero:
    bio = hero.short_bio.lower() 
    if 'time-traveling' in bio or 'suit' in bio:
        print(f"{hero.name}: {hero.short_bio}")

print ('**************************************************************')

nombres_a_eliminar = ['Electro', 'Baron Zemo']

for nombre in nombres_a_eliminar:
    pos = list_superhero.search(nombre, 'name')
    if pos is not None:
        eliminado = list_superhero.pop(pos)
        print(f"Se eliminó: {eliminado.name}, {eliminado.real_name} - {'Villano' if eliminado.is_villain else 'Héroe'}")
    else:
        print(f"{nombre} no está en la lista.")


