# This is a really bad way to do this but it works

from utils import *

start_time: float = get_start_time()

import day01
import day02
import day03

print_time_elapsed(start_time, "Total runtime")
