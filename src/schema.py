from pydantic import BaseModel, validator
import typing


class ZombieWorld(BaseModel):
    """
    Schema for the POST request
    """

    dimension: int
    position: typing.Dict[str, int]
    creatures: typing.List
    moves: str

    @validator("position")
    def position_must_in_the_grid(cls, v, values):
        if v["x"] > values["dimension"] or v["y"] > values["dimension"]:
            raise ValueError("Position out of range")
        return v

    @validator("creatures")
    def creatures_must_in_the_grid(cls, v, values):
        for creature in v:
            if creature[0] > values["dimension"] or creature[1] > values["dimension"]:
                raise ValueError("Creature is not in the grid")
        return v

    @validator("moves")
    def moves_must_be_in_the_grid(cls, v):
        for charachter in v.lower():
            if charachter not in ["r", "d", "u"]:
                raise ValueError("Invalid input - Allowed directions are r, u, and d")
        return v
