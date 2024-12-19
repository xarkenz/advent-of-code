const std = @import("std");

fn lessThan(context: void, a: i32, b: i32) bool {
    _ = context;
    return a < b;
}

pub fn run(input_path: []const u8, allocator: std.mem.Allocator) !void {
    const std_out = std.io.getStdOut().writer();
    var input_file = try std.fs.cwd().openFile(input_path, .{});
    defer input_file.close();

    var reader = std.io.bufferedReader(input_file.reader());

    var line = std.ArrayList(u8).init(allocator);
    defer line.deinit();

    var left_nums = std.ArrayList(i32).init(allocator);
    var right_nums = std.ArrayList(i32).init(allocator);

    while (true) {
        reader.reader().streamUntilDelimiter(line.writer(), '\n', null) catch |err| switch (err) {
            error.EndOfStream => break,
            else => return err,
        };
        if (line.getLastOrNull()) |last| {
            if (last == '\r') {
                _ = line.pop();
            }
        }

        var iter = std.mem.splitSequence(u8, line.items, "   ");
        const left_str = iter.first();
        const right_str = iter.rest();
        const left = try std.fmt.parseInt(i32, left_str, 10);
        const right = try std.fmt.parseInt(i32, right_str, 10);

        try left_nums.append(left);
        try right_nums.append(right);

        line.clearRetainingCapacity();
    }

    std.sort.insertion(i32, left_nums.items, {}, lessThan);
    std.sort.insertion(i32, right_nums.items, {}, lessThan);

    var total_distance: i32 = 0;
    for (left_nums.items, right_nums.items) |left, right| {
        total_distance += @intCast(@abs(left - right));
    }

    try std_out.print("[01p1] Total distance: {d}\n", .{total_distance});

    var similarity_score: i32 = 0;
    for (left_nums.items) |left| {
        for (right_nums.items) |right| {
            if (left == right) {
                similarity_score += left;
            }
        }
    }

    try std_out.print("[01p2] Similarity score: {d}\n", .{similarity_score});
}
