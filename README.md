# Introduction

Thanks amazingly Ailo for providing such an interesting practice. 

This file will describe 

1. What the practice is about
2. How to run it
3. Testing

## Rules of the Zombie World
The world is represented by an n x n grid on which zombies and creatures live.
The location of zombies and creatures can be addressed using zero-indexed x-y
coordinates. The top left corner of the world is (x: 0, y: 0). The horizontal coordinate
is represented by x, and the vertical coordinate is represented by y.

At the beginning of the program, a single zombie awakes and begins to move around the
grid following a sequence of movements. Valid movements are Up, Down, Left, Right. The
movement sequence is represented by a string of single character movements, e.g. RDRU
(Right, Down, Right, Up).
Zombies can move through the edge of the grid, appearing on the directly opposite side. For
a 10x10 grid, a zombie moving left from (0, 4) will move to (9, 4); a zombie moving down
from (3, 9) will move to (3, 0).

The creatures are aware of the zombie’s presence but are so frightened that they never
move.

Once a zombie has completed its movement, the first newly created zombie moves using
the same sequence as the original zombie, then the second newly created zombie moves,
and so on, in order of infection. Each zombie performs the same sequence of moves. Once
all zombies have completed moving, the final positions of all zombies and creatures should
be output, then the program ends.

# Start
## Prerequisite
1. [Docker](https://docs.docker.com/engine/install/)

## Run the app
```
$ docker-compose build
``` 

```
$ docker-compose up
```
## URLs

### **[API Document presented by Swagger - 127.0.0.1:3000/docs](http://127.0.0.1:3000/docs)**
> Please read the document first.


Landing page
```
GET http://127.0.0.1:3000/zombie_world
```
Run the Zombie World with POST request
```
POST http://127.0.0.1:3000/zombie_world/start
```
## Request
```json
{
    "dimension": 5,
    "position" : {"x": 0 , "y": 0},
    "creatures": [[0, 1], [1, 1], [3, 0]],
    "moves": "uurdrd"
}
```
## Response
```json
{
    "messages": [
        "zombie 0 moved from (0, 0) to (0, 1)",
        "Creature got infected at - (0, 1)",
        "zombie 0 moved from (0, 1) to (0, 2)",
        "zombie 0 moved from (0, 2) to (1, 2)",
        "zombie 0 moved from (1, 2) to (1, 1)",
        "Creature got infected at - (1, 1)",
        "zombie 0 moved from (1, 1) to (2, 1)",
        "zombie 0 moved from (2, 1) to (2, 0)",
        "zombie 1 moved from (0, 0) to (0, 1)",
        "zombie 1 moved from (0, 1) to (0, 2)",
        "zombie 1 moved from (0, 2) to (1, 2)",
        "zombie 1 moved from (1, 2) to (1, 1)",
        "zombie 1 moved from (1, 1) to (2, 1)",
        "zombie 1 moved from (2, 1) to (2, 0)",
        "zombie 2 moved from (0, 0) to (0, 1)",
        "zombie 2 moved from (0, 1) to (0, 2)",
        ...
        ...
        ...
    ]
}
```
## Tests

Run all the tests
```
$ pytest 
```

Run one single file
```
$ pytest <file_location> // pytest src/test_zombie_world.py
```

Run one single test
```
$ pytest <file_location>::<test_name> // pytest src/test_zombie_world.py::test_zombie_world_success
```
## Operate with Docker
```
$ docker ps // Check IMAGE ailo_ailo is on the list
```
```
$ docker exec -it ailo_ailo_1 bash
```
#### Reformat 
```
# black <file_name> // or just '.' to reformat all the files
```