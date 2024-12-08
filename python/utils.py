from dataclasses import dataclass
from typing import Iterator, Union
import time

# General Utilities

start_time: float = time.time()

def print_time_elapsed(label: str = "Time elapsed"):
    global start_time
    print(f"{label}: {(time.time() - start_time) * 1000:.3f} ms")

def get_input_text(filename: str) -> str:
    with open(f"input/{filename}") as input_file:
        return input_file.read()

def get_input_lines(filename: str) -> list[str]:
    with open(f"input/{filename}") as input_file:
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

# Tile Map Utilities

@dataclass
class Point:
    row: int
    col: int

    def manhattan_distance_to(self, other: "Point") -> int:
        return abs(self.row - other[0]) + abs(self.col - other[1])
    
    def rotate_90_cw(self) -> "Point":
        return Point(self.col, -self.row)
    
    def rotate_90_ccw(self) -> "Point":
        return Point(-self.col, self.row)

    def __getitem__(self, index: int) -> int:
        return [self.row, self.col].__getitem__(index)

    def __iter__(self) -> Iterator[int]:
        return [self.row, self.col].__iter__()

    def __add__(self, other: "Point") -> "Point":
        return Point(self.row + other[0], self.col + other[1])
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.row - other[0], self.col - other[1])
    
    def __mul__(self, scalar: int) -> "Point":
        return Point(self.row * scalar, self.col * scalar)
    
    def __hash__(self) -> int:
        return (self.row, self.col).__hash__()

class TileMapRow:
    def __init__(self, filler_tile: str = " "):
        self.filler_tile: str = filler_tile
        self.tiles: str = ""
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
    
    def __getitem__(self, col: Union[int, slice]) -> str:
        if isinstance(col, slice):
            start = col.start if col.start is not None else (self.min_col() if col.step is None or col.step > 0 else self.max_col())
            stop = col.stop if col.stop is not None else (self.max_col() + 1 if col.step is None or col.step > 0 else self.min_col() - 1)
            step = col.step if col.step is not None else 1
            return "".join(self.get(slice_col) for slice_col in range(start, stop, step))
        else:
            return self.get(col)

    def put(self, col: int, tiles: str) -> str:
        if len(self.tiles) == 0:
            self.first_col = col
            self.tiles = tiles
        else:
            # eugh
            new_tiles = ""
            if self.first_col < col:
                new_first_col = self.first_col
                new_tiles += self.tiles[:min(len(self.tiles), col - self.first_col)]
                if new_first_col + len(new_tiles) < col:
                    new_tiles += self.filler_tile * (col - (new_first_col + len(new_tiles)))
            else:
                new_first_col = col
            new_tiles += tiles
            if new_first_col + len(new_tiles) < self.first_col + len(self.tiles):
                if new_first_col + len(new_tiles) < self.first_col:
                    new_tiles += self.filler_tile * (self.first_col - (new_first_col + len(new_tiles)))
                new_tiles += self.tiles[max(0, (new_first_col + len(new_tiles)) - self.first_col):]
            self.first_col = new_first_col
            self.tiles = new_tiles
    
    def copy(self) -> "TileMapRow":
        copy = TileMapRow(self.filler_tile)
        copy.tiles = self.tiles
        copy.first_col = self.first_col
        return copy

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

    def get(self, point: Point) -> str:
        row = point[0]
        col = point[1]
        if self.min_row() <= row <= self.max_row():
            return self.rows[row].get(col)
        else:
            return self.filler_tile
    
    def put(self, point: Point, tiles: str):
        row = point[0]
        col = point[1]
        if row > self.max_row():
            self.rows.extend(TileMapRow(self.filler_tile) for _ in range(row - self.max_row()))
        elif row < self.min_row():
            self.rows[0:0] = (TileMapRow(self.filler_tile) for _ in range(self.min_row() - row))
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
        points_iter = (Point(self.first_row + row_index, col) for row_index in range(len(self.rows)) for col in self.rows[row_index].col_range())
        raw_iter = ((point, self.get(point)) for point in points_iter)
        return ((point, tile) for point, tile in raw_iter if tile != self.filler_tile)
    
    def __str__(self) -> str:
        return "\n".join(tile_row[self.min_col() : self.max_col() + 1] for tile_row in self.rows)
