from dataclasses import dataclass

def gcd(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

@dataclass
class Point:
    row: int
    col: int

    def manhattan_distance_to(self, other):
        return abs(self.row - other[0]) + abs(self.col - other[1])

    def __getitem__(self, index):
        return [self.row, self.col].__getitem__(index)

    def __iter__(self):
        return [self.row, self.col].__iter__()

    def __add__(self, other):
        return Point(self.row + other[0], self.col + other[1])
    
    def __sub__(self, other):
        return Point(self.row - other[0], self.col - other[1])
    
    def __mul__(self, scalar):
        return Point(self.row * scalar, self.col * scalar)

class TileMapRow:
    def __init__(self):
        self.tiles = ""
        self.col_offset = 0

    def put_tiles(self, col, tiles):
        if len(self.tiles) == 0:
            self.col_offset = col
            self.tiles = tiles
        else:
            pass

class TileMap:
    def __init__(self, filler_tile):
        self.filler_tile = filler_tile
        self.rows = []
        self.row_offset = 0
        self.min_col = 0
        self.max_col = -1
    
    def put_row(self, point, tiles):
        pass
