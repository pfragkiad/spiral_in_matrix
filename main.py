
from enum import Enum


class Direction(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


class Rotation(Enum):
    CLOCKWISE = 1
    COUNTERCLOCKWISE = 2

from typing import Generator, Any

def getSpiralMatrix(a: list[list[int]], i: int, j: int, rot: Rotation, dir: Direction) -> Generator[Any, Any, None]:
    rows, cols = len(a), len(a[0])
    maxi, maxj = rows - 1,  cols - 1
    mini = minj = 0

    while (mini <= maxi and minj <= maxj):
        yield a[i][j]
  
        if dir == Direction.RIGHT:
            if j < maxj:
                j += 1
                continue
            if rot == Rotation.CLOCKWISE:
                i += 1
                mini += 1
                dir = Direction.DOWN
            else:
                i -= 1
                maxi -= 1
                dir = Direction.UP
        elif dir == Direction.DOWN:
            if i < maxi:
                i += 1
                continue
            if rot == Rotation.CLOCKWISE:
                j -= 1
                maxj -= 1
                dir = Direction.LEFT
            else:
                j += 1
                minj += 1
                dir = Direction.RIGHT
        elif dir == Direction.LEFT: 
            if j > minj:
                j -= 1
                continue
            if rot == Rotation.CLOCKWISE:
                i -= 1
                maxi -= 1
                dir = Direction.UP
            else:
                i += 1
                mini += 1
                dir = Direction.DOWN
        elif dir == Direction.UP: 
            if i > mini:
                i -= 1
                continue
            if rot == Rotation.CLOCKWISE:
                j += 1
                minj += 1
                dir = Direction.RIGHT
            else:
                j -= 1
                maxj -= 1
                dir = Direction.LEFT


# a: list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a: list[list[int]] = [[1, 2, 3, 4], [5, 6, 7, 8],
                      [9, 10, 11, 12], [13, 14, 15, 16]]
# a= [[1,2],[3,4]]
# a = [[1, 2, 3, 4]]
rot: Rotation = Rotation.COUNTERCLOCKWISE
dir: Direction = Direction.DOWN if rot == Rotation.CLOCKWISE else Direction.LEFT
i, j = 0, 3

spiral = list(getSpiralMatrix(a, i, j, rot, dir))
for el in spiral:
    print(el)

