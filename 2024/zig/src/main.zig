const std = @import("std");

const day01 = @import("day01.zig").run;

const input_dir = "./input/";

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};

    try day01(input_dir ++ "day01.txt", gpa.allocator());
}
