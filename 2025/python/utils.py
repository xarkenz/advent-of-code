import sys
from pathlib import Path

# Add the common directory to sys.path and import the actual utils module
sys.path.insert(0, str(Path(__file__).resolve().parents[2].joinpath("common")))
from aoc_utils import *
