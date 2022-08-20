from zombie_world import zombie_world
from zombie_objects import Position, Grid, Creature, Move
import pytest


@pytest.mark.parametrize(
    "grid,position,creatures,move,message,expected",
    [
        (
            Grid(4),
            Position(Grid(4).dimension, 3, 1),
            [
                Creature(Grid(4).dimension, 0, 1),
                Creature(Grid(4).dimension, 1, 2),
                Creature(Grid(4).dimension, 1, 1),
            ],
            Move(Grid(4).dimension, "rdru"),
            [],
            23,
        ),
        (
            Grid(4),
            Position(Grid(4).dimension, 0, 0),
            [
                Creature(Grid(4).dimension, 0, 1),
                Creature(Grid(4).dimension, 3, 0),
                Creature(Grid(4).dimension, 4, 2),
            ],
            Move(Grid(4).dimension, "u"),
            [],
            2,
        ),
        (
            Grid(5),
            Position(Grid(4).dimension, 1, 0),
            [
                Creature(Grid(4).dimension, 0, 1),
                Creature(Grid(4).dimension, 0, 0),
                Creature(Grid(4).dimension, 4, 2),
            ],
            Move(Grid(4).dimension, "rruuudr"),
            [],
            8,
        ),
    ],
)
def test_zombie_world_success(grid, position, creatures, move, message, expected):
    result = zombie_world(
        grid=grid,
        position=position,
        creatures=creatures,
        move=move,
        messages=message,
    )
    assert len(result) == expected


def test_zombie_world_failed_with_position_out_of_grid():
    with pytest.raises(Exception) as exc:
        zombie_world(
            grid=Grid(4),
            position=Position(Grid(4).dimension, 4, 1),
            creatures=[
                Creature(Grid(4).dimension, 0, 1),
                Creature(Grid(4).dimension, 3, 0),
                Creature(Grid(4).dimension, 4, 2),
            ],
            move=Move(Grid(4).dimension, "rdruu"),
            messages=[],
        )
    assert str(exc.value) == "Position is invalid"


def test_zombie_world_failed_with_creature_outside_the_grid():
    with pytest.raises(Exception) as exc:
        Creature(Grid(4).dimension, 5, 2)

    assert str(exc.value) == "Creature is not in the grid"


def test_zombie_world_failed_with_invalid_position():
    with pytest.raises(Exception) as exc:
        Position(Grid(4).dimension, 4, 2)

    assert str(exc.value) == "Position is invalid"
