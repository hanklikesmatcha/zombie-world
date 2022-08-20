from zombie_world import _zombie_move, zombie_world
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
            4,
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
            10,
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


def test_zombie_world_no_creatures_survived():
    _, zombies, creatures = _zombie_move(
        grid=Grid(2),
        initial_position=Position(Grid(2).dimension, x=0, y=0),
        creatures=[Creature(Grid(2).dimension, x=1, y=1)],
        move=Move(Grid(2).dimension, "ru"),
        messages=[],
    )
    assert len(zombies) == 1
    assert zombies[0].location == (1, 1)
    assert len(creatures) == 0


def test_zombie_world_one_creature_survived():
    _, zombies, survived_creatures = _zombie_move(
        grid=Grid(5),
        initial_position=Position(Grid(5).dimension, x=0, y=0),
        creatures=[
            Creature(Grid(5).dimension, x=2, y=2),
            Creature(Grid(5).dimension, x=2, y=0),
        ],
        move=Move(Grid(5).dimension, "rdrd"),
        messages=[],
    )
    assert len(zombies) == 1
    assert zombies[0].location == (2, 2)
    assert len(survived_creatures) == 1
    assert survived_creatures[0].location == (2, 0)
