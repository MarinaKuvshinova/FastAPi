from pydantic import BaseModel, validator



class PokemonState(BaseModel):
    pokemon_id: int
    height_m: float
    weight_kg: float
    attack: int

class PokemonStateResponseModel(PokemonState):
    id: int

    class Config():
        orm_mode = True


class Pokemon(BaseModel):
    name: str
    classification: str
    type1: str
    type2: str
    generation: int
    is_legendary: int
    stats: PokemonStateResponseModel

    @validator("name")
    def title_mustbe_min_3_characters(cls, v):
        if len(v) < 3:
            raise ValueError("Title must be at least 3 characters")

        return v

class PokemonResponseModel(Pokemon):
    id: int

    class Config():
        orm_mode = True
