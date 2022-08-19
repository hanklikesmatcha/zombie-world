import json
from zombie_objects import Creature, Grid, Position, Move
from fastapi import FastAPI, Response, HTTPException, Request
import uvicorn
from zombie_world import zombie_world
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schema import ZombieWorld

app = FastAPI()


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=jsonable_encoder(
            {"code": 500, "message": f"Internal Server Error - {exc}"}
        ),
    )


@app.get("/zombie_world")
def index():
    return dict(data="Welcome to the zombie world")


@app.post("/zombie_world/start")
def ailo(request: ZombieWorld):
    """
    Zombie will start from the initial position and make steps based on the values from the moves.
    If the Zombie find a Creature on the way, the Creature becomes a Zombie.

    :parm dimension:Integer. Define the coverage of the moves.
    :parm creatures: A list of string. The sad folks who might get infected in the game.
    :parm position: A list of string: Where the Zombie starts..
    :parm moves: String. To direct where will the first Zombie move.
    :return A list of messages in json format
    """
    grid = Grid(request.dimension)
    position = Position(grid.dimension, request.position["x"], request.position["y"])
    creatures = [Creature(grid.dimension, c[0], c[1]) for c in request.creatures]
    move = Move(grid.dimension, request.moves.lower())
    try:
        messages = zombie_world(
            grid=grid, position=position, creatures=creatures, move=move
        )
        response = {"messages": messages}
    except Exception as error:
        raise HTTPException(
            status_code=422, detail={"error_messages": f"Invalid inputs - {str(error)}"}
        )
    return Response(content=json.dumps(response), media_type="application/json")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
