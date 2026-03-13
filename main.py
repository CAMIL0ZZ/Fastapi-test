from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pokemon(BaseModel):
    id: int
    name: str
    attack: int
    life: int
    type: str


pokemons = [
    Pokemon(id=1,name="Bulbasaur",attack=49,life=45,type="grass"),
    Pokemon(id=4,name="Charmander",attack=52,life=39,type="fire"),
    Pokemon(id=7,name="Squirtle",attack=48,life=44,type="water"),
    Pokemon(id=25,name="Pikachu",attack=55,life=35,type="electric"),
    Pokemon(id=6,name="Charizard",attack=84,life=78,type="fire")
]


@app.get("/pokemon/{id}")
def get_pokemon(id: int):

    for p in pokemons:

        if p.id == id:
            return p

    return {"error": "pokemon not found"}


@app.get("/battle")
def battle(id1: int, id2: int):

    p1 = None
    p2 = None

    # BUSCAR LOS DOS POKEMON
    for p in pokemons:

        if p.id == id1:
            p1 = p

        if p.id == id2:
            p2 = p

    # VALIDAR SI EXISTEN
    if p1 is None or p2 is None:
        return {"error": "pokemon not found"}

    # DETERMINAR GANADOR
    if p1.attack >= p2.attack:
        winner = p1
    else:
        winner = p2

    return {
        "pokemon1": p1.name,
        "pokemon2": p2.name,
        "winner": winner.name
    }

@app.get("/pokemons")
def get_pokemons(name: str = "", order_by: str = "id"):

    result = []

    # FILTRAR POR NOMBRE
    for p in pokemons:

        # si no se envía nombre devuelve todos
        if name == "":
            result.append(p)

        else:
            if name.lower() in p.name.lower():
                result.append(p)

    # ORDENAR RESULTADOS
    for i in range(len(result)):
        for j in range(i + 1, len(result)):

            value_i = getattr(result[i], order_by)
            value_j = getattr(result[j], order_by)

            if value_i > value_j:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result

