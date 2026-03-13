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
