from collections import Counter


class Grid:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.row = dimension
        self.col = dimension


class Position(Grid):
    def __init__(self, dimension: int, x: int, y: int):
        super().__init__(dimension=dimension)
        if x > self.row or x < 0 or y > self.col or y < 0:
            raise Exception("Position is not in the grid")
        self.x = x
        self.y = y

    @property
    def where(self) -> tuple:
        return (self.x, self.y)


class Creature(Grid):
    def __init__(self, dimension: int, x: int, y: int):
        super().__init__(dimension=dimension)
        if x > self.row or y > self.col:
            raise Exception("Creature is not in the grid")
        self.x = x
        self.y = y

    @property
    def location(self) -> tuple:
        return (self.x, self.y)


class Move(Grid):
    def __init__(self, dimension: int, move: str):
        super().__init__(dimension=dimension)
        move = move.lower()
        for charachter in move:
            if charachter not in ["r", "d", "u"]:
                raise Exception(f"Invalid Direction - {charachter}")
        counter = Counter(move)
        for v in dict(counter).values():
            if v > self.dimension:
                raise Exception(f"Invliad position")
        self.steps = move
