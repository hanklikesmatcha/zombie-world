import typing
from zombie_objects import Creature, Grid, Position, Move


def _check_infection(creatures: typing.List[Creature], position: Position) -> tuple:
    infected_creatures = []
    safe_creatures = []
    messages = []
    for creature in creatures:
        if position.where == creature.location:
            messages.append(f"Creature got infected at - {position.where}")
            infected_creatures.append(creature)
        else:
            safe_creatures.append(creature)
    return infected_creatures, safe_creatures, messages


def _zombie_move(
    grid: Grid,
    initial_position: Position,
    creatures: typing.List[Creature],
    move: Move,
    messages: typing.List[str],
    round: int = 0,
) -> tuple:
    prepare_for_next_step = initial_position
    new_messages = messages
    new_zombies = []
    safe_creatures = creatures
    for _, step in enumerate(move.steps):
        if step == "r":
            create_new_move = Position(
                grid.dimension,
                0
                if prepare_for_next_step.x + 1 == grid.dimension
                else prepare_for_next_step.x + 1,
                prepare_for_next_step.y,
            )
            has_moved = create_new_move
            new_messages.append(
                f"zombie {round} moved from {prepare_for_next_step.where} to {has_moved.where}"
            )
            prepare_for_next_step = has_moved
            infected_creatures, safe_creatures, sos_messages = _check_infection(
                creatures=safe_creatures, position=has_moved
            )
            for z in infected_creatures:
                if z:
                    new_zombies.append(z)
            for m in sos_messages:
                if m:
                    new_messages.append(m)
        if step == "d":
            create_new_move = Position(
                grid.dimension,
                prepare_for_next_step.x,
                0
                if prepare_for_next_step.y - 1 == grid.dimension
                else prepare_for_next_step.y + 1,
            )
            has_moved = create_new_move
            new_messages.append(
                f"zombie {round} moved from {prepare_for_next_step.where} to {has_moved.where}"
            )
            prepare_for_next_step = has_moved
            infected_creatures, safe_creatures, sos_messages = _check_infection(
                creatures=safe_creatures, position=has_moved
            )

            for z in infected_creatures:
                if z:
                    new_zombies.append(z)
            for m in sos_messages:
                if m:
                    new_messages.append(m)

        if step == "u":
            create_new_move = Position(
                grid.dimension,
                prepare_for_next_step.x,
                grid.dimension - 1
                if prepare_for_next_step.y - 1 == -1
                else prepare_for_next_step.y - 1,
            )
            has_moved = create_new_move
            new_messages.append(
                f"zombie {round} moved from {prepare_for_next_step.where} to {has_moved.where}"
            )
            prepare_for_next_step = has_moved
            infected_creatures, safe_creatures, sos_messages = _check_infection(
                creatures=safe_creatures, position=has_moved
            )
            for z in infected_creatures:
                if z:
                    new_zombies.append(z)
            for m in sos_messages:
                if m:
                    new_messages.append(m)
    final_safe_creatures = safe_creatures
    if len(final_safe_creatures) == 0:
        message_from_creatures = f"No leftover Creatures :'("
        new_messages.append(message_from_creatures)
    else:
        for c in final_safe_creatures:
            message_from_creatures = (
                f"Creature located on {c.location} survived this round."
            )
            new_messages.append(message_from_creatures)

    return new_messages, new_zombies, final_safe_creatures


def zombie_world(
    grid: Grid,
    position: Position,
    creatures: typing.List[Creature],
    move: Move,
    messages: typing.List[str] = [],
) -> typing.List[str]:
    """
    Zombie will start from the initial position and make steps based on the values from the move.
    If the Zombie find a Creature on the way, the Creature becomes a Zombie.

    :parm grid: Grid object. Define the coverage of the move.
    :parm position: Position object.  Where the Zombie starts.
    :parm creatures: A list of Creature objects: The sad folks who might get infected in the game.
    :parm move: A list of Move objects. It can be a single object, but having a list here in case zombie wants to have a long walk.
    :parm messages: A list of messages. To document all the Zombie's move and where the Creatures become a Zombie.
    :return A list of messages
    """
    try:
        messages, zombies, _ = _zombie_move(
            grid=grid,
            initial_position=position,
            creatures=creatures,
            move=move,
            messages=[],
        )
        if len(zombies) != 0:
            for i in range(len(zombies)):
                _zombie_move(
                    grid=grid,
                    initial_position=Position(
                        grid.dimension, zombies[i].x, zombies[i].y
                    ),
                    creatures=[],
                    move=move,
                    messages=messages,
                    round=i + 1,
                )
    except Exception as e:
        raise Exception(e)
    return messages
