from dataclasses import dataclass, field
from typing import *
import time
import heapq

# General Utilities

def get_start_time() -> float:
    return time.time()

def print_time_elapsed(start_time: float, label: str = "Time elapsed"):
    print(f"{label}: {(time.time() - start_time) * 1000:.3f} ms")

def get_input_text(filename: str) -> str:
    with open(f"../input/{filename}") as input_file:
        return input_file.read()

def get_input_lines(filename: str) -> list[str]:
    with open(f"../input/{filename}") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        while lines and not lines[-1]:
            lines.pop()
        return lines

def get_input_tile_map(filename: str) -> "TileMap":
    tile_map = TileMap()
    for row, line in enumerate(get_input_lines(filename)):
        tile_map.put((row, 0), line)
    return tile_map

# Math Utilities

def gcd(a: int, b: int) -> int:
    while b > 0:
        (a, b) = (b, a % b)
    return a

def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b

# Data Structures

# Basically just a wrapper around heapq methods for convenience
_T = TypeVar("_T")
class MinHeap(Generic[_T]):
    items: list[_T]

    def __init__(self, items: Optional[list[_T]] = None) -> None:
        if items is not None:
            heapq.heapify(items)
            self.items = items
        else:
            self.items = []
    
    def push(self, item: _T) -> None:
        heapq.heappush(self.items, item)
    
    def pop(self) -> _T:
        return heapq.heappop(self.items)

    def peek(self) -> _T:
        return self.items[0]
    
    def __bool__(self) -> bool:
        return bool(self.items)

# Tile Map Utilities

PointLike: TypeAlias = Union["Point", tuple[int, int]]

@dataclass
class Point:
    row: int
    col: int

    def manhattan_distance_to(self, other: PointLike) -> int:
        return abs(self.row - other[0]) + abs(self.col - other[1])
    
    def rotate_90_cw(self) -> "Point":
        return Point(self.col, -self.row)
    
    def rotate_90_ccw(self) -> "Point":
        return Point(-self.col, self.row)

    def __getitem__(self, index: int) -> int:
        return [self.row, self.col].__getitem__(index)

    def __iter__(self) -> Iterator[int]:
        return [self.row, self.col].__iter__()

    def __add__(self, other: PointLike) -> "Point":
        return Point(self.row + other[0], self.col + other[1])
    
    def __sub__(self, other: PointLike) -> "Point":
        return Point(self.row - other[0], self.col - other[1])
    
    def __mul__(self, scalar: int) -> "Point":
        return Point(self.row * scalar, self.col * scalar)
    
    def __hash__(self) -> int:
        return (self.row, self.col).__hash__()

class TileMapRow:
    def __init__(self, row: int, filler_tile: str = " "):
        self.filler_tile: str = filler_tile
        self.row: int = row
        self.tiles: list[str] = []
        self.first_col: int = 0
    
    def min_col(self) -> int:
        return self.first_col
    
    def max_col(self) -> int:
        return self.first_col + len(self.tiles) - 1

    def col_range(self) -> range:
        return range(self.first_col, self.first_col + len(self.tiles))
    
    def get(self, col: int) -> str:
        if self.min_col() <= col <= self.max_col():
            return self.tiles[col - self.first_col]
        else:
            return self.filler_tile

    def put(self, col: int, tiles: Sequence[str]):
        if len(self.tiles) == 0:
            self.first_col = col
            self.tiles.extend(tiles)
        elif len(tiles) > 0:
            index = col - self.first_col
            if index < 0:
                self.tiles[0:0] = (self.filler_tile for _ in range(-index))
                self.first_col = col
                index = 0
            elif index > len(self.tiles):
                self.tiles.extend(self.filler_tile for _ in range(index - len(self.tiles)))
            if len(tiles) == 1:
                if index == len(self.tiles):
                    self.tiles.append(tiles[0])
                else:
                    self.tiles[index] = tiles[0]
            else:
                end_index = min(len(self.tiles), index + len(tiles))
                self.tiles[index : end_index] = tiles
    
    def copy(self) -> "TileMapRow":
        copy = TileMapRow(self.row, self.filler_tile)
        copy.tiles = self.tiles.copy()
        copy.first_col = self.first_col
        return copy
    
    def __iter__(self) -> Iterator[tuple[Point, str]]:
        return iter((Point(self.row, col), tile) for col, tile in zip(self.col_range(), self.tiles) if tile != self.filler_tile)

class TileMap:
    def __init__(self, filler_tile: str = " "):
        self.filler_tile: str = filler_tile
        self.rows: list[TileMapRow] = []
        self.first_row: int = 0
        self.cached_min_col: int = 0
        self.cached_max_col: int = -1
    
    def min_row(self) -> int:
        return self.first_row
    
    def max_row(self) -> int:
        return self.first_row + len(self.rows) - 1

    def min_col(self) -> int:
        return self.cached_min_col
    
    def max_col(self) -> int:
        return self.cached_max_col

    def get(self, point: PointLike) -> str:
        row = point[0]
        col = point[1]
        if self.min_row() <= row <= self.max_row():
            return self.rows[row].get(col)
        else:
            return self.filler_tile
    
    def put(self, point: PointLike, tiles: str):
        row = point[0]
        col = point[1]
        if row > self.max_row():
            self.rows.extend(TileMapRow(self.max_row() + 1 + offset, self.filler_tile) for offset in range(row - self.max_row()))
        elif row < self.min_row():
            self.rows[0:0] = (TileMapRow(row + offset, self.filler_tile) for offset in range(self.min_row() - row))
        self.rows[row].put(col, tiles)
        self.cached_min_col = min(self.cached_min_col, self.rows[row].min_col())
        self.cached_max_col = max(self.cached_max_col, self.rows[row].max_col())
    
    def copy(self) -> "TileMap":
        copy = TileMap(self.filler_tile)
        copy.rows = [row.copy() for row in self.rows]
        copy.first_row = self.first_row
        copy.cached_min_col = self.cached_min_col
        copy.cached_max_col = self.cached_max_col
        return copy
    
    def __iter__(self) -> Iterator[tuple[Point, str]]:
        return iter(item for row in self.rows for item in row)
    
    def __str__(self) -> str:
        return "\n".join(tile_row[self.min_col() : self.max_col() + 1] for tile_row in self.rows)
